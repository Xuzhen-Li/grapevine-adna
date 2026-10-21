## aDNA 捕获测试：处理流程（脱敏笔记）

原始笔记里的下载凭据、数据路径、合同号、fastq 链接和样本列表都已删除。对应脚本在 `scripts/`。

### 1. 输入
- 每个样本是双端 fastq：`<SAMPLE>_1.fq.gz` / `<SAMPLE>_2.fq.gz`（dsDNA 批次用 `<SAMPLE>_R1.fastq.gz` / `_R2`）。
- 参考基因组：`<REF_DIR>/VS1.final.fa`。

### 2. 每个样本的流程（`scripts/adna_capture_pipeline_generator.sh` 为每个样本生成一个 Slurm 脚本）
1. AdapterRemoval：`--trimqualities --minquality 2 --trimns --minlength 25 --collapse`（dsDNA 批次 `--minlength 30`）
2. bwa aln `-l 1024 -n 0.01`（dsDNA 批次 `-l 1000`）+ bwa samse（写入 @RG）
3. samtools：转 BAM → flagstat → `-F4` 只留比对上的 reads → sort/index
4. `samtools view -q 30` 质量过滤 → flagstat → sort/index
5. picard CleanSam + MarkDuplicates（`REMOVE_DUPLICATES=TRUE`）→ index/flagstat
6. qualimap bamqc
7. mapDamage `-i <dedup.bam> -r <REF_DIR>/VS1.final.fa -d <SAMPLE>_damage`

### 3. 汇总
`scripts/collect_mapping_stats.sh`：从 flagstat 和 qualimap 输出里取 RawReads、MappedReads、Q30Reads、DupReads、DedupBases，写进 `stats.all.tsv`。

### 4. 整理目录
处理完把每个样本的文件移进各自目录：`mkdir -p <SAMPLE> && mv <SAMPLE>* <SAMPLE>/`
