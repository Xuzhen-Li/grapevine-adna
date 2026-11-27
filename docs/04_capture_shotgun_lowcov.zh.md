# 4. 捕获还是鸟枪法，以及低覆盖度分型

库通过第一轮损伤查看之后，还要决定是加深鸟枪法测序还是做捕获，以及低覆盖度下如何（以及不要如何）分型或补全。这里的命令来自打开过的 README 或论文，不是我们跑过的葡萄默认值。

Ramos-Madrigal 等（2019，摘要）和 Cohen 等（2023，全文）都对考古葡萄种子使用了“靶向富集的全基因组测序”。现有目录已记录针对葡萄 SNP 面板的液相捕获；各篇论文实际用的探针数量应以该文 Methods 为准，这里不猜测。Cohen 等 2023（2026-11-15 CST 重开全文，PMC10151551）写：样本 A31–A37 的文库 “were enriched for a set of 10,207 SNPs according to Ramos-Madrigal et al. ( 22 ) and Laucou et al. ( 28 )。” 因此 10,207 这一数字取自 Cohen 2023。Ramos-Madrigal 2019 或 Laucou 2018 本身是否写出该数，2026-11-15 CST 未重开，标 **[待确认]**。Noraz 等 2026（2026-11-15 CST 重开全文，PMC13013926）中没有这个数字。现有目录里把 10,207 写成 Ramos-Madrigal / Laucou 事实、或同时把 Noraz 当作该数出处的行，本次更新不改，只在目录末尾追加勘误。Noraz 等（2026，全文）报告 49 粒种子的“全基因组古代 DNA 数据”；捕获还是鸟枪法的细节应读 Methods，不能只凭摘要断定（若只用摘要，标为 **[待确认]**）。

Carpenter 等（2013，摘要）是全基因组捕获方法论文，数据集偏向人类，只作捕获方法引用，不是葡萄探针设计。Wales 等（2012，摘要）给出筛查准备做鸟枪法测序的古代植物遗存的一种低成本试验，不是葡萄捕获设计。Bolognesi 等（2025，全文）讲的是如何从考古葡萄种子里多回收可处理的古代 DNA，不能代替筛查之后在捕获和鸟枪法之间的选择。现有 WORKFLOW 的分法是：先浅测或小规模筛查看内源含量和损伤，可用后再加深测序或捕获，然后重新比对和去重再分型。本组教学章节打开的来源中没有任何一篇给出葡萄种子“必须”转捕获的数值门槛（**[待确认]**）。

Schubert 等（2012，2026-11-15 CST 打开全文，PMC3468387）是现有 WORKFLOW 里 `bwa aln -l 1024` 在 Illumina 数据上关闭种子搜索的出处。原文写：“For both Illumina and Helicos sequencing data, the seed was disabled in the optimized set of mapping parameters (−l 1024)。” 同一篇还写 BWA 的 “-n option, with a default value of 0.04”。`-n 0.01 -o 2` 仍按 WORKFLOW 的写法归为人类古代 DNA 里常见的组合，Green 等 2010 的原始出处仍为 **[待确认]**，那不是 Schubert 写明的默认值。本章不把这些参数混成新的“葡萄默认值”。仓库里的捕获生成脚本（`scripts/adna_capture_pipeline_generator.sh`，见 REMOVALS.md）用 `-l 1024 -n 0.01` 和 AdapterRemoval `--minlength 25`。`scripts/dsdna_preprocess.sh`（亦见 REMOVALS.md）用 `-l 1000`，第 12 行是 `--minlength 30`。WORKFLOW 里 AdapterRemoval 的默认值是 `--minlength 30`。2026-11-15 CST 打开的 AdapterRemoval 文档里，软件自身的长度默认值是 15：v2.3.4 手册是 `--minlength`，“Defaults to 15.”；3.0.2 手册（https://adapterremoval.readthedocs.io/en/v3.0.2/manpage.html）是 `--min-length`，同一句 “Defaults to 15.”。这些数值不在这里当作新标准。

ANGSD（README 已打开）仍是目录里首选的似然途径。很低覆盖度时不要强行做二倍体硬分型，以及伪单倍体随机抽取（sequenceTools pileupCaller）会丢掉个体内杂合、不能直接当作杂合度估计，这两句是本仓库的教学判断，不是已打开的 ANGSD 或 sequenceTools 摘要或 README 里的原句。单链文库时，现有 WORKFLOW 已指向 `pileupCaller --singleStrandMode`；打开的 sequenceTools README 把该选项写成实验功能，并说明配合合并后的读段使用，正式运行前应再对照该 README。

Rubinacci 等（2023，全文，PMC10335927）把 GLIMPSE2 写成对 150,119 个英国生物银行基因组的低覆盖度补全。那是人类数据集。GLIMPSE 的 README 记录的是从单倍型参考面板做低覆盖度补全。现有 WORKFLOW 已规定：只有在现代葡萄上下采样到古代深度、并预先登记准确率测试（AM17，项目 20）之后，才允许对葡萄做补全。预登记仍需写死深度网格、按 MAF 分档的 r² 和通过线；参考面板必须去掉测试个体的克隆和一级亲属（本仓库的设计要求，写成正式方案前仍标 **[待确认]**）。本章不编一套葡萄 GLIMPSE2 参数，也不把英国生物银行的准确率数字当成葡萄的数字。

READv2 和 KIN 是低覆盖度亲缘工具。Noraz 等 2026（2026-11-15 CST 重开全文）在 Methods 里叙述 READv2 的 P0 步骤后写：“This procedure was, however, originally developed for human data and may, thus, not immediately apply to species with high heterozygosity and mixed sexual and clonal reproduction systems, such as grapevine.” 这句话说的是该文中的 READv2，不是 KIN README 的原句。

KIN 仓库 README（2026-11-15 CST 重取，8,590 字节，sha256 d8fb5c88…）把 `-N` 写在 “Running KINgaroo” 节下，而不是 “Running KIN” 节。原文是：“N: Total number of chromosome pairs. Default=22”。它没有写 22 是人类常染色体数。同一节还要求 BAM 染色体名为 “1,2,..,X,Y”；葡萄组装常用 chr01 这类名字，这是本仓库的提醒，不是 README 原句。

Canaguier 等 2017（2026-11-15 CST 已打开全文，PMC5612791，doi:10.1016/j.gdata.2017.09.002）写：“The v2 chromosome assembly therefore consists of 19 chromosome sequences (chr01 to chr19) and one chromosome random pseudo-molecule (chr00)。” 把 KINgaroo 的 `-N` 设为 19 以对应这 19 条染色体，是依据该句的本仓库判断；KIN README 没有提到葡萄或 19，作为 Vitis 的工具默认值仍标 **[待确认]**。Jaillon 等 2007 的摘要（2026-11-15 CST 已打开）没有写出染色体数目，不用作 19 的出处。

Noraz 等 2026 已有葡萄 READv2 校准：P0=0.238，仅用于 ACG / vinifera；sylvestris 另设阈值；假阳性率 0.4%；克隆识别 99.3%/94.6%。其中 identical 类是用伪单倍化重复构造的。该校准是否按古样本深度降采样，仍标 **[待确认]**。READv2 默认中位数归一化假定多数样本对无关，克隆多的材料会违背这一前提，更稳妥的是固定 P0 并按群分开（本仓库判断）。种子组织来源（种皮还是胚）会影响“完全相同”的判定，WORKFLOW 已有提醒，对葡萄仍标 **[待确认]**。现代 SNP 上的 KING 硬分型门槛不能直接搬到古代深度。

论断—出处表见 [04_capture_shotgun_lowcov.md](04_capture_shotgun_lowcov.md)。
