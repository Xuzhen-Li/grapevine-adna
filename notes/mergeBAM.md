## 找到到处分布的"*.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam"

```bash
find ./ -type f -name "*.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam" | sort
```
```
<DATA_DIR>/<batch>/<SAMPLE>/<SAMPLE>.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam
# ...（原始样本路径列表已删除）
```
make a bam list

## samtools合并
```bash 
#生成命令
awk '
  {
      # 提取纯数字编号
      if (match($0, /SAMPLE_[0-9]+/)) {
          id = substr($0, RSTART+7, RLENGTH-7) + 0   # 去掉前缀并转数字
          file[id] = file[id] " " $0
      }
  }
  END {
      for (i=1; i<=19; i++)
          printf "samtools merge -@ 8 merged_bams/SAMPLE_%d.merged.bam%s\n", i, file[i]
  }' bam_list.txt > merge_cmds.sh

## 命令样式
samtools merge -@ 8 merged_bams/SAMPLE_01.merged.bam <bam_1> <bam_2> ...

# pao
bash merge_cmd.sh
```


## 重新去重复 统计 索引 damage
```bash
#!/bin/bash
#SBATCH --job-name=rmdup
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH -p <PARTITION>
#SBATCH -o rmdup.out
#SBATCH -e rmdup.err
for i in {1..19}
do
samtools index SAMPLE_${i}.merged.bam
picard CleanSam INPUT=SAMPLE_${i}.merged.bam OUTPUT=SAMPLE_${i}.merged.clean.bam
picard MarkDuplicates INPUT=SAMPLE_${i}.merged.clean.bam OUTPUT=SAMPLE_${i}.merged.rmdup.MarkD.bam REMOVE_DUPLICATES=TRUE AS=TRUE METRICS_FILE=SAMPLE_${i}.merged.rmdup.MarkD.metics VALIDATION_STRINGENCY=SILENT 
samtools index SAMPLE_${i}.merged.rmdup.MarkD.bam
samtools flagstat SAMPLE_${i}.merged.rmdup.MarkD.bam  > SAMPLE_${i}.merged.rmdup.MarkD.stats
qualimap bamqc -bam SAMPLE_${i}.merged.rmdup.MarkD.bam -nt 10 -outformat HTML
mapDamage -i SAMPLE_${i}.merged.rmdup.MarkD.bam -r <REF_DIR>/VS1.final.fa -d ${i}_damage
done
```


mapDamage -i ${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam -r <REF_DIR>/VS1.final.fa -d ${F}_damage



## reheader
```bash
for bam in SAMPLE_{1..19}.merged.rmdup.MarkD.bam; do
    sid=$(basename $bam .merged.rmdup.MarkD.bam)

    # 重新写头，把所有 RG 的 SM 统一成当前样本名
    samtools reheader -c \
      'perl -pe "s/SM:\S+/SM:'$sid'/g"' \
      "$bam" > ${sid}.merged.rmdup.MarkD.fixed.bam

    samtools index ${sid}.merged.rmdup.MarkD.fixed.bam
done

## gatk calling(4.3.0)
```bash
#!/bin/bash
#SBATCH --job-name=gvcf
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=36
#SBATCH -p <PARTITION>
#SBATCH -o gvcf.out
#SBATCH -e gvcf.err
ref=<REF_DIR>/VS1.final.fa        
threads=24
mkdir -p gvcf

for bam in SAMPLE_{1..19}.merged.rmdup.MarkD.fixed.bam ; do
    sid=$(basename $bam .merged.rmdup.MarkD.fixed.bam)      # SAMPLE_1, SAMPLE_2, ...
    gvcf=gvcf/${sid}.g.vcf.gz
    gatk --java-options "-Xmx8g" \
        HaplotypeCaller \
         -R $ref \
         -I $bam \
         -O $gvcf \
         -ERC GVCF \
         -A StrandOddsRatio \
         -A Coverage \
         -A QualByDepth \
         -A FisherStrand \
         -A MappingQualityRankSumTest \
         -A ReadPosRankSumTest \
         -A RMSMappingQuality \
         --pair-hmm-threads $threads
done



```
