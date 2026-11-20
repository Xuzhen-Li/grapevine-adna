# 2. 损伤鉴定

损伤模式用来判断比对上的读段是否像古代分子。下面的工具都来自本组教学章节打开的论文或 GitHub README。它们单独都不能宣布一份葡萄样本“鉴定通过”。

Ginolhac 等（2011，摘要；doi:10.1093/bioinformatics/btr347；刊期 2011，在线 2011-06-09）是 mapDamage 的原文，题为测试古代 DNA 序列中的损伤模式，Crossref 与 EuropePMC 题名一致。Jónsson 等（2013，2026-11-15 CST 重开摘要，全文先前记录为 PMC3694634）把 mapDamage 2.0 写成对古代 DNA 损伤参数做快速近似贝叶斯估计。同一摘要写：“Our model enables rescaling base quality scores according to their probability of being damaged.” 2026-11-15 CST 打开的 GitHub README（https://github.com/ginolhac/mapDamage，1,995 字节，sha256 b87e12ee…）只在指向专门文档页时提到 “plotting, modeling, and rescaling”，本身并没有描述会调整碱基质量的命令模式。因此碱基质量重标定引自 mapDamage 2.0 论文摘要，不引自 README。本仓库已有的薄封装 `scripts/run_mapdamage.sh` 第 6 行原文是 `mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences`（见 REMOVALS.md，建议保留），但不能代替阅读 mapDamage 2.0 文档。

Skoglund 等（2014，摘要）用死后损伤把内源古代 DNA 和现代污染分开，这是 PMDtools 的来源。DamageProfiler（Neukamm 等 2021，doi:10.1093/bioinformatics/btab190；README 3,850 字节，2026-11-15 CST 已打开）是一种损伤模式计算工具，也出现在 nf-core/eager 的说明里。pyDamage 按 contig 估计损伤，打开的 README 和论文把它用于宏基因组；不能把它写成竞争性比对工具，也不是葡萄专用鉴定器。

已打开的 Briggs 和 Rohland 摘要支持损伤集中在分子末端。双链 / 单链 / 半 UDG 的具体对应关系（包括末端一两个碱基的残余损伤）在本次追加打开的文本和现有 WORKFLOW.md 里都不是现成的句子，仍标 **[待确认]**。半 UDG 应引用 Rohland 等那篇的原文。把“半 UDG 后两端各剪 2 nt”当作葡萄默认值，在没有对应文库类型的出处之前标为 **[待确认]**。

Briggs 等（2010，全文，PMC2847228）题为去除古代 DNA 中的脱氨胞嘧啶并检测体内甲基化。全文写 USER（UDG 加内切酶 VIII）去除尿嘧啶，并且 “Neandertal DNA retains in vivo patterns of CpG methylation”。这是尼安德特人 DNA 上的 CpG 甲基化结果。本组教学章节打开的来源中没有把这句话推广到植物 CG、CHG 或 CHH 的来源。植物上下文里全 UDG 后仍有残余 C-to-T 的说法，标为 **[待确认]**。现有 WORKFLOW 里关于植物 CG/CHG/CHH 的那句，本章不作为已核实事实再写一遍。

Weiß 等（2016，摘要和全文，PMC4929915）研究植物标本馆标本 DNA 的损伤随时间变化和降解动力学。Porrelli 等（2026，摘要）是后续的标本馆损伤论文。它们都不是考古葡萄种子数据集，但与植物历史 DNA 如何降解有关。

论断—出处表见 [02_authentication_damage.md](02_authentication_damage.md)。
