# REMOVALS.zh.md — 已从本仓库移除的文件

下列三个捕获测试脚本已从仓库中移除。`scripts/02_map_adna.sh` 和 `scripts/03_dedup.sh` 未改。帮助 / `--dry-run` 封装 `scripts/02_map_adna.v2.sh` 和 `scripts/03_dedup.v2.sh` 仍保留。`scripts/run_mapdamage.sh` 仍保留。

## 已移除

- `scripts/adna_capture_pipeline_generator.sh`：占位样本名；用 heredoc 为每个样本生成 Slurm 脚本；AdapterRemoval `--minlength 25`，与 WORKFLOW 默认 30 不一致；只对 collapsed 读段做 `bwa aln -l 1024 -n 0.01`，随后用 Picard `CleanSam` + `MarkDuplicates` 而不是 DeDup；分区是硬编码的占位符 `<PARTITION>`；未比对未合并的双端。`collapsed.truncated` 是否未比对，标为 **[待确认]**。教学上由 `02_map_adna.v2.sh`、`03_dedup.v2.sh`（仅帮助 / `--dry-run`）和 WORKFLOW 决策树覆盖比对和去重；mapDamage 由 `run_mapdamage.sh` 承担。新流程若用 DeDup，需写明读名前缀 `M_` / `F_` / `R_`。没有替代的部分：每样本 Slurm 脚本生成、原生成器中的 AdapterRemoval 命令和参数、`@RG`、各阶段 flagstat、Qualimap。正式流程应写成新文件。
- `scripts/dsdna_preprocess.sh`：循环变量写成了 `FLIES`；`bwa aln -l 1000 -n 0.01`，与原生成器的 `-l 1024` 和 WORKFLOW 的 `-l 1024` 都不一致；同样走 Picard MarkDuplicates。脚本头是 `#SBATCH --cpus-per-task=40`，每一步却用 35 个线程。分区同样是硬编码占位符。若仍需要双链预处理脚本，应新写文件。
- `scripts/collect_mapping_stats.sh`：占位样本名单；每次运行先清空 `stats.all.tsv` 和 `stats_debug.log` 再追加；用 grep/awk 解析 flagstat 和 Qualimap。列含义依赖 flagstat 的措辞。原生成器写出 `*.collapsed.stats`，该脚本却读 `*.mapped.stats`，这些字段会变成 NA。`DupReads` 列实际是去重后保留的读数，不是被去掉的重复数。如仍需要汇总，应新写并测试。02/03 封装并不替代 Qualimap 或各阶段 flagstat。

## 仍保留在仓库中

- `scripts/00_sim_damaged_fastq.py` 至 `07_authentication_summary.py`、`run_toy_pipeline.sh`、`testdata/`：玩具流程。脚本 README 记录了哪些步骤经过测试。模拟器只种了 5-prime C-to-T，不能代表双链、单链或 UDG 文库。
- `scripts/run_mapdamage.sh`：很薄的 mapDamage2 封装。第 6 行原文是 `mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences`。
- 主 README、`docs/WORKFLOW.md`（及中文）、`catalog/CATALOG.tsv`、`scripts/README.md`：现有教学和流程文本。
- `notes/` 下已脱敏的笔记：记录当时怎么跑，不当作正式流程。`mergeBAM.md` 里还有 GATK HaplotypeCaller 的 gVCF 循环，不是第 4 章讲的低覆盖度路径。

## 从已移除脚本中记下的参数

旧脚本里引用的参数（例如 `-l 1024 -n 0.01` 与 `-l 1000`，`--minlength 25` 与 WORKFLOW 默认的 30）写在这里，是为了避免把它们混成新的默认值。WORKFLOW 已经提醒不要把脚本里的值和文献设置混在一起。

已移除的双链预处理脚本在第 12 行使用 `--minlength 30`，与 WORKFLOW 默认值一致；已移除的生成器使用 `--minlength 25`。
