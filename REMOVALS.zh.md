# REMOVALS.md — 建议淘汰清单（本次追加不删除任何文件）

请仓库所有者在任何会删除文件的拉取请求之前先看这份清单。本次追加在 live 的 `README.md`、`README.zh.md` 和 `catalog/CATALOG.tsv` 末尾追加内容，并新增教学文件。不修改 live 的 `scripts/02_map_adna.sh` 和 `scripts/03_dedup.sh`。README 和目录里已有的每一行都保持原样。新的封装版本是 `scripts/02_map_adna.v2.sh` 和 `scripts/03_dedup.v2.sh`。下列脚本在仓库所有者批准删除之前仍留在仓库里。

逐个文件的阅读是在提交 b6e4302e（2026-11-15 17:29 CST）的 inventory 副本上做的。查阅该副本时只用 `git --no-optional-locks rev-parse` / `ls-files`，不对它运行 `git status`。下面的路径相对于仓库根目录。

## 两个选项（由仓库所有者决定；这里什么都不删）

- **方案 A.** 把三个脚本移到 `scripts/legacy/`，在原路径留下简短 stub，标明“历史记录，不推荐”。下列交叉引用届时需要改一行，否则会断：中英文 README 约第 385 行、`scripts/README.md` 第 5–7 行、CATALOG A14、ADDITIONS 第 60 行、`notes/cap_test.md` 第 9 和 19 行、`docs/04_capture_shotgun_lowcov.md` 第 23 行（比对提醒里点名了生成器和 `dsdna_preprocess.sh`）和第 55 行（声明–出处表中对应行）、`docs/04_capture_shotgun_lowcov.zh.md` 第 9 行、`SOURCES_READ.tsv` 第 88 行、`CHANGELOG.md` 第 13 行。
- **方案 B.** 脚本留在原处，只在文件开头加同样的“历史记录，不推荐”说明。**在生产流程审完之前，方案 B 更稳妥，也是本次追加的建议。** 新的 `scripts/02_map_adna.v2.sh` 和 `scripts/03_dedup.v2.sh` 只是帮助 / `--dry-run` 文档，还不能替代原来的捕获测试记录。live 的 `scripts/02_map_adna.sh` 和 `scripts/03_dedup.sh` 保持逐字节不变。

## 建议保留

- `scripts/00_sim_damaged_fastq.py` 至 `07_authentication_summary.py`、`run_toy_pipeline.sh`、`testdata/`：新合并的玩具流程。脚本 README 记录了哪些步骤经过测试。模拟器只种了 5′ 端 C-to-T，不能代表双链、单链或 UDG 文库。
- `scripts/run_mapdamage.sh`：很薄的 mapDamage2 封装。第 6 行原文是 `mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences`。它是旧脚本里 mapDamage 那一步的替代，仍然适合作为这一步的包装。
- 主 README、`docs/WORKFLOW.md`（及中文）、`catalog/CATALOG.tsv`、`scripts/README.md`：现有教学和流程文本。本次追加只在 live README 和目录末尾追加，不替换已有各行。
- `notes/` 下已脱敏的笔记：记录当时怎么跑，不当作正式流程。`mergeBAM.md` 里还有 GATK HaplotypeCaller 的 gVCF 循环，不是第 4 章讲的低覆盖度路径。

## 建议淘汰（只列表，不删除）

- `scripts/adna_capture_pipeline_generator.sh`：占位样本名；用 heredoc 为每个样本生成 Slurm 脚本；AdapterRemoval `--minlength 25`，与 WORKFLOW 默认 30 不一致；只对 collapsed 读段做 `bwa aln -l 1024 -n 0.01`，随后用 Picard `CleanSam` + `MarkDuplicates` 而不是 DeDup；分区是硬编码的占位符 `<PARTITION>`；未比对未合并的双端。`collapsed.truncated` 是否未比对，标为 **[待确认]**。教学上由 `02_map_adna.v2.sh`、`03_dedup.v2.sh`（仅帮助 / `--dry-run`）和 WORKFLOW 决策树覆盖比对和去重；mapDamage 由 `run_mapdamage.sh` 承担。新流程若用 DeDup，需写明读名前缀 `M_` / `F_` / `R_`。**没有替代的部分：** 每样本 Slurm 脚本生成、生成器第 32–44 行的 AdapterRemoval 命令和参数、第 56 行的 `@RG`、各阶段 flagstat、Qualimap。正式流程应在审查后写成新文件，不要在删除的同时悄悄改这份生成器。
- `scripts/dsdna_preprocess.sh`：循环变量写成了 `FLIES`（`ls … \| sed`）；`bwa aln -l 1000 -n 0.01`，与生成器的 `-l 1024` 和 WORKFLOW 的 `-l 1024` 都不一致；同样走 Picard MarkDuplicates。脚本头是 `#SBATCH --cpus-per-task=40`（第 5 行），第 12–27 行每一步（AdapterRemoval、bwa、samtools、Qualimap）都用 35 个线程。分区同样是硬编码占位符。没有出处说它是“后加的”。若仍需要双链预处理脚本，应新写文件。
- `scripts/collect_mapping_stats.sh`：占位样本名单；每次运行先用 `>` 清空 `stats.all.tsv` 和 `stats_debug.log` 再追加；用 grep/awk 解析 flagstat 和 Qualimap，并用 `head -n 10` 把文件开头拷进调试日志。列含义依赖 flagstat 的措辞，措辞一变就容易错。生成器写出 `*.collapsed.stats`，collect 却读 `*.mapped.stats`，这些字段会变成 NA。`DupReads` 列实际是去重后保留的读数，不是被去掉的重复数。如仍需要汇总，应新写并测试。02/03 封装并不替代 Qualimap 或各阶段 flagstat。

## 不是删除提案

旧脚本里引用的参数（例如 `-l 1024 -n 0.01` 与 `-l 1000`，`--minlength 25` 与 WORKFLOW 默认的 30）写在这里，是为了避免把它们混成新的默认值。WORKFLOW 已经提醒不要把脚本里的值和文献设置混在一起。

`dsdna_preprocess.sh` 第 12 行使用 `--minlength 30`，与 WORKFLOW 默认值一致；生成器使用 `--minlength 25`。

这里列出的文件在本次追加中没有被删除、移动或改名。
