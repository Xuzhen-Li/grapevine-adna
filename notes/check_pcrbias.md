## 确定找一下pcr bias

# 通过samtools view -q 过滤是不可靠的，它本质上是比对质量，是统计值。也就是MAPQ，比对质量，比对错误的潜在概率，和测序质量类似。多重比对的过滤是另外一回事
# 我的preprocess部分，已经collapsed了，因为aDNA很短，所以collapsed的比例很大。truncated就很小，就相当于单链了，bwa aln和 bwa sames就是单链比对的方法。所有我的bam中只有0 4 16.
# damge pattern 是pcr过程中产生的，u被放大了
# 关于udg处理，UDG（Uracil-DNA Glycosylase） 会把 所有 U（尿嘧啶） 切除 → 留下无碱基位点 → 测序时变成 N 或 缺失。但 CpG 上下文里的 C→U 由于 甲基化保护，逃脱 UDG 切除 → 仍被保留下来 → 仍能观察到 C→T / G→A 损伤。因此 UDG+ 文库 的 唯一可观测损伤信号 就只剩 CpG 位点。
# 至于之前试验中gc含量激增的原因，末端修复完成后，所有的U被完全切除掉了，只剩下CpG岛里的，被切除后的有gap的地方也会进行测序（通过气泡相连），但是会在测序结果中产生N，另一条链是A还是？空缺会不计数，额外的AT减少了。少了一部分CG，cpg岛里的gc还保留，多伦扩增以后激增？


## 确定postAMP和preAMP前后，包括cp的
直接找到在基因组上新增加的位点和reads？提取这些reads，看看damage pattern，判断哪些是pcr产生的bias，哪些是pcr扩增出来的样本？

关注“扩增后新出现的 unique reads”里  
1. **真正古 DNA 分子被扩出来**
2. **PCR 偏向（bias）新造出来的假分子**，  
核心思路是：**利用古 DNA 特有的末端损伤信号 + 分子坐标信息** 做“损伤-坐标双标记”过滤。

**但是基于目前的情况也不一定，PCR扩出来的reads正确的情况下C变U，U和A互补，T和A互补，导致G2A，C2T的比例越扩越多。如果是非特异性扩增比如在cPg岛附近无法扩增，非特异性扩增出来其他reads的话，他就是属于gcta的比率会保持不变？**
| 步骤                  | GC %               |
| ------------------- | ------------------ |
| 原始古库（UDG-）          | ~40 %    本来就偏低，因为U的存在导致AT增加          |
| UDG+（正常）            | ~45 %    AT本身不变， GC相对原先增加了，U被去除了         |
| **UDG 过度**（长时间/高酶量） | **> 55 %** 甚至 60 % ，U被全部去除了 |


## 末端修复后，adapter前
| 组分            | 终浓度             | 作用                                           |
| ------------- | --------------- | -------------------------------------------- |
| **UDG**       | 0.2–0.5 U/μL    | 切除 **U** → 产生 abasic 位点                      |
| **Endo VIII** | 0.2 U/μL        | **裂解 abasic 位点 3' 侧磷酸二酯键** → 形成 **1 nt gap** |
| **Buffer**    | 1× Quick Repair | 提供 Mg²⁺、pH 7.5–8.0                           |


## CpG岛的问题
1. 古DNA UDG处理后，C>T 列即 CpG → TpG 比例；G>A 即 CpG → CpA（互补链）
2. ref.CpG.bed 可用 bedtools intersect ref.fa.bed <(echo -e "C\tG") 生成，或下载 UCSC CpG islands。
3. 现代二代测序数据，怎么找CpG岛
 
| 数据类型                | 是否需亚硫酸盐转化 | 分辨率  | 推荐路线                                     |
| ------------------- | --------- | ---- | ---------------------------------------- |
| **WGBS/RRBS**       | ✅（已转化）    | 单碱基  | 直接 `bismark` → `methylKit`               |
| **常规 WGS/RNA/Chip** | ❌（无转化）    | 区域/峰 | `macs2`/`deeptools` 找 **覆盖度** 或 **peak** |

坐标可以UCSC Table Browser → 选 CpG Islands → 下载 cpgIslandExt.txt

## pmdtools的用法
```bash
$ pmdtools -help
Usage: python pmdtools <SAM formatted data with MD field present from stdin> [options] 

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --adjustss            strand orientation aware penalization of base
                        qualities for single stranded libraries (use with
                        --CpG for udg-treated ss libs)
  -n MAXREADS, --number=MAXREADS
                        stop after these many reads have been processed
  -c CHROMOSOME, --chromosome=CHROMOSOME
                        only process data from this chromosome
  -m MAPQ, --requiremapq=MAPQ
                        only process sequences with mapping quality at least
                        this great
  --readlength=READLENGTH
                        only process sequences with this read length
  --maxlength=MAXLENGTH
                        only process sequences with max this read length
  --minlength=MINLENGTH
                        only process sequences with min this read length
  --maxGC=MAXGC         only process sequences with max this GC content of the
                        aligning reference sequence
  --minGC=MINGC         only process sequences with min this GC content of the
                        aligning reference sequence
  -q BASEQ, --requirebaseq=BASEQ
                        only process bases with base quality at least this
                        great
  -d, --deamination     output base frequencies in the read at positions where
                        there are C or G in the reference
  --CpG, --UDGplus      only use Cs and Gs in CpG context
  --ss                  single stranded
  --PMDSprim            PMDSprim
  --PMDSprimthreshold=PMDSPRIMTHRESHOLD
                        PMDSprimthreshold
  --UDGhalf             only use Cs and Gs in CpG context, the first and last
                        base are used regardless of dinucleotide context
  --UDGminus            use all bases (placeholder)
  --EcoliCpG            Ecoli CpG (first 5' position and two 3' positions and
                        CpG context)
  --Ecoli               Ecoli (first 5' position and two 3' positions only)
  --maskss              mask to lower case bases where ref is C (taking strand
                        into account)
  --Leipzigsimple       Leipzigsimple
  --customterminus=CUSTOMTERMINUS
                        customterminus
  --flagss              flag SNPs (taking strand into account)
  --noCpG               dont use Cs and Gs in CpG context
  --first               outputs the deamination rate at the first position
                        only, but with a standard error
  --range=RANGE         output deamination patterns for this many positions
                        from the sequence terminus (default=30)
  --polymorphism_ancient=POLYMORPHISM_ANCIENT
                        True biological polymorphism between the ancient
                        individual and the reference sequence
  --polymorphism_contamination=POLYMORPHISM_CONTAMINATION
                        True biological polymorphism between the contaminants
                        and the reference sequence
  --PMDpparam=PMDPPARAM
                        parameter p in geometric probability distribution of
                        PMD
  --PMDconstant=PMDCONSTANT
                        constant C in geometric probability distribution of
                        PMD
  --noclips             no clips
  --noindels            no indels
  --onlyclips           only clips
  --onlydeletions       only deletions
  --onlyinsertions      only insertions
  --nodeletions         no deletions
  --noinsertions        no insertions
  --notreverse          no reverse complement alignments
  -p, --printDS         print PMD scores
  --verbose             verbose
  --printalignments     print human readable alignments
  --maskterminaldeaminations=MASKTERMINALDEAMINATIONS
                        mask terminal deaminations
  --maskterminalbases=MASKTERMINALBASES
                        mask terminal bases
  -t THRESHOLD, --threshold=THRESHOLD
                        only output sequences with PMD score above this
                        threshold
  --upperthreshold=UPPERTHRESHOLD
                        only output sequences with PMD score below this
                        threshold
  --perc_identity=PERC_IDENTITY
                        only output sequences with percent identity above this
                        threshold
  -a, --adjustbaseq     apply PMD-aware adjustment of base quality scores
                        specific to C>T and G>A mismatches to the reference
  --adjustbaseq_all     apply PMD-aware adjustment of base quality scores
                        regardless of observed bases
  --dry                 print SAM input without any filters
  --samtoolspath=SAMTOOLSPATH
                        full path to samtools
  --basecomposition     basecomposition
  -r REFSEQ, --refseq=REFSEQ
                        refseq
  --header              output the SAM header
  --estimate            two-terminus estimate of contamination
  --estimatebase=ESTIMATEBASE
                        position of base used fortwo-terminus estimate of
                        contamination
  --platypus            output big list of base frequencies for platypus
  --writesamfield       add 'DS:Z:<PMDS>' field to SAM output, will overwrite
                        if already present
  -b BASIC, --basic=BASIC
                        only output reads with a C>T mismatch this many
                        basepairs from the 5' end
  --terminal            only output reads with a C>T mismatch in either 3' or
                        5' end
  --stats               output summarizing statistics to stderr
  ```


# test data(https://www.ebi.ac.uk/ena/browser/view/PRJEB86428)
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/run/ERR147/ERR14766763/I0992.bam
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/run/ERR147/ERR14766763/I0992.bam.bai


### data pre
- **同一古库**  
  - **pre-PCR 测序** → `pre.bam`  
  - **post-PCR 测序** → `post.bam`  
- 已比对、已去 adapter、已去 duplicate（**保留 duplicate 信息**？）
---
### 1. PMDtools给reads估计损伤分数
1. 测试好久不通，浪费了两天时间，软件本身小问题很多，比如你只想输出ds评分是不行的，你要加上-t 0才可以，不然输出永远都是空的，我却用了这么长时间没检查出来，不要懒多试试
```bash
# 用 PMDtools 给两个 BAM 都加 DP 标签（0=无损伤，>3 高损伤）
## 例子
samtools view -h SAMPLE_A.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam | pmdtools --writesamfield -t --20 --header --ss | samtools view -b -o SAMPLE_A.pmd.bam
samtools view -h SAMPLE_A-Amp-CB.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam | pmdtools --writesamfield -t -20 --header --ss | samtools view -b -o SAMPLE_Aampcp.pmd.bam
samtools view -h SAMPLE_A-OG-CB.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam | pmdtools --writesamfield -t -20 --header --ss | samtools view -b -o SAMPLE_Acp.pmd.bam
samtools view -h SAMPLE_A-Amp.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam | pmdtools --writesamfield -t 20 --header --ss | samtools view -b -o SAMPLE_Aamp.pmd.bam

samtools view I0992.pmd.bam | \
awk '{
    # 从最后一列提取DS值（假设格式为DS:Z:数字）
    if (split($NF, a, ":") >= 3) {
        ds_value = a[3] + 0;  # 转换为数字
        bucket = int(ds_value);  # 向下取整确定区间
        count[bucket]++;  # 统计
    }
}
END {
    # 输出分布
    for (b in count) 
        printf "区间 [%d, %d): %d 个读数\n", b, b+1, count[b];
}'
### 这个分数很奇怪，测试了古葡萄，现代葡萄，古人类，都是一样的分布模式？



```
---
### 2.找出“post 比 pre 多出来”的 reads
```bash
# 以 read name 为键，取差集
samtools view -F 0x904 pre.pmd.bam | cut -f1 | sort -u > pre.names
samtools view -F 0x904 post.pmd.bam | cut -f1 | sort -u > post.names
grep -F -x -v -f pre.names post.names > extra.names   # 多出来的
# 提取多出来的 BAM
samtools view -@ 8 -F 0x904 -N extra.names -b post.pmd.bam > extra.bam
```

------------------------------------------------
### 3.“多出来”的reads分类
#    ancient_real : 坐标已存在 + 高损伤
#    ancient_novel: 坐标全新 + 高损伤
#    bias_novel   : 坐标全新 + 低损伤
```bash
samtools view -h extra.bam | \
awk -v coords="pre.coords.bed" '
  BEGIN{while((getline<coords)>0) bed[$1"\t"$2"\t"$3]=1}
  function inBed(c,s,e){for(k in bed){split(k,a,"\t");if(a[1]==c && s<a[3] && e>a[2])return 1} return 0}
  /^@/{print; next}
  (and($2,0x800)||and($2,0x100)||and($2,0x4)){next}
  {dp=0;for(i=12;i<=NF;i++)if($i~/^DP:i:/){dp=substr($i,6);break}
   chr=$3; start=$4-1; end=$4+length($10);
   ancient = (inBed(chr,start,end) && dp>=3);
   novelHi = (!inBed(chr,start,end) && dp>=3);
   novelLo = (!inBed(chr,start,end) && dp<3)
  }
  ancient     {print > "ancient_real.sam"}
  novelHi     {print > "ancient_novel.sam"}
  novelLo     {print > "bias_novel.sam"}'

for f in ancient_real ancient_novel bias_novel; do
  samtools view -b ${f}.sam > ${f}.bam
  rm ${f}.sam
done
```

---------------------------------------------

#!/bin/bash
set -e
ref=<REF_DIR>/VS1.final.fa
  mapDamage -i SAMPLE_A.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam \
            -r $ref \
            -d SAMPLE_A_dmg \
            --rescale
            --rescale-out SAMPLE_A.rescale.bam \
            --rescale-length-5p 5 \
            --rescale-length-3p 5 \
  samtools index SAMPLE_A.rescale.bam



----- 
ngs briggs
```bash
Usage
./ngsBriggs -bam -tab -ref -bed -len -chr -ibam -iref -ibed -ichr -obam -otab -oinf -olen -model -eps -isrecal -olik -nthreads
	-> -bam: The bam file for inference;
	-> -tab: The table file for inference;
	-> -ref: The reference file for inference;
	-> -bed: The bed file (1-based) for inference;
	-> -len: The length mass probability distribution file for inference;
	-> -chr: The focal chromosome for inference;
	-> -ibam: The bam file for ancient strand fishing;
	-> -iref: The reference file for ancient strand fishing;
	-> -ibed: The bed file (1-based) for ancient strand fishing;
	-> -ichr: The focal chromosome for ancient strand fishing;
	-> -obam: The output bam file name;
	-> -otab: The output table file name;
	-> -oinf: The output inferred parameters file name;
	-> -olen: The output length mass probability distribution file name;
	-> -model: Specifying the model, either b (the biotin model) or nb (the non-biotin model);
	-> -eps: The overall modern contamination rate, the value should be within the interval [0,1);
	-> -isrecal: Choose 1 if recalibration based on length is needed, otherwise 0 (default);
	-> -olik: The output nucleotide likelihood file;
	-> -nthreads: Choose the number of threads to speed up the recalibration process.

Example

Inference of Briggs parameters with three different ways
./ngsbriggs -bam Chr22_024_36_68_0097.sorted.MD.bam -ref chr22.fa -model nb
./ngsbriggs -model nb -bdamage Chr22_024_36_68_0097.bdamage.gz -rlens Chr22_024_36_68_0097.rlens.gz
./ngsbriggs -tab mismatch2.txt -len len.txt -model nb

Inference of Briggs parameters with epsilon
./ngsbriggs -bam Chr22_024_36_68_0097_eps10.sorted.MD.bam -ref chr22.fa -eps 0.1 -model nb

Decontamination with epsilon
./ngsbriggs -bam Chr22_024_36_68_0097_eps10.sorted.MD.coord.bam -model nb -eps 0.1 -ibam Chr22_024_36_68_0097_eps10.sorted.MD.coord.bam -obam Chr22_024_36_68_0097_eps10.sorted.MD.scores.bam -isrecal 1 -ibed chr22.bed -chr chr22 -nthread 1

If recal = 0, we calculate the posterior probability (AN) solely based on deamination patterns (within 30 bp); If recal = 1, we will also consider the length distribution when estimating AN, and A0 is the same as AN in the case recal = 0.
```



# 其他
# 2 线粒体诊断位点
python mdd_score.py -b ancient.pmd.bam -bed diag40.bed -mt
# 3 性染色体
python xy_contam.py -b ancient.pmd.bam --sex female
# 4 ML 常染色体(核心原理还是线粒体推测)
angsd -i ancient.pmd.bam -doContam 1 -out ancient -minsize 500