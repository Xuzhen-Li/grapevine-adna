# 3. 污染检查（以及为什么 hapCon 不是葡萄方案）

在葡萄研究实验室里，现代葡萄 DNA 和人的 DNA 一样都是污染风险。本章工具都来自打开过的论文或 README。其中不少是为人的数据写的，不能当作葡萄方法来用。

Huang 和 Ringbauer（2022，全文，PMC9344841）把 hapCon 写成“估计男性现代人古代 DNA 污染”的新方法，使用单倍体 X 染色体上的 Li&Stephens 单倍型拷贝模型。hapROH/hapCon 的 README 写：“hapCon is an extension of hapROH for estimating contamination rate for male aDNA samples。”本组教学章节打开的来源里，没有与之相当的葡萄 X 染色体设计。目录里收录 hapCon，只是为了防止误用。我们不编一套葡萄版 hapCon。

hapROH（Ringbauer 等 2021，全文）用单倍型参考面板从低覆盖度数据估计纯合连续区，设计和测试都在人类数据上，这里不把它写成现成的葡萄克隆历史工具。

Peyrégne 和 Peter（2020，摘要）把 AuthentiCT 写成估计单链文库古代 DNA 数据中现代 DNA 污染比例的工具，只依据死后损伤模式，少至约 10,000 条已比对序列即可。打开的 README 原话是：只适用于单链文库产生的序列，不针对双链文库更复杂的脱氨模式；也不能估计经过 UDG 或其他会改变脱氨模式的酶处理的样本；同样原因，不能在“只保留已脱氨序列”的过滤数据集上估计污染。README 还写该方法假定污染物本身没有脱氨。

schmutzi（Renaud 等 2015，doi:10.1186/s13059-015-0776-0）是一套污染估计工具。2026-11-15 CST 重新取回了官方 README（38,285 字节，sha256 e85cb02b…，2026-11-15 CST）。README 写 contDeam 的默认做法 “is useful for all types of ancient DNA (nuclear and mitonchondrial)” [sic]。Nuclear 一节写：核样本推荐用 DICE；schmutzi 对核数据能做的只是凭脱氨模式估计污染率，并且 “use this at your own risk”，同时列出导致估计错误的前提（分子数至少 500M、内源脱氨 upwards of 5%、污染物片段几乎没有脱氨、5′ 与 3′ 脱氨相互独立等）。污染物若也脱氨，会低估。线粒体还可以用 mtCont 交叉验证，核数据不能。本章不再把“不是葡萄核基因组污染工具”写成硬性适用范围。葡萄核文库是否满足这些前提，本次追加未测试，标为 **[待确认]**。README 把默认候选库写成 “197 human mitogenomes” 的全球抽样，这一库是面向人类的。FAQ 还提到 USER/UDG 处理可以解释看不到脱氨模式。现有目录里 schmutzi 那一行（live b6e4302e 的 A10）仍是旧表述，本次追加不改该行，只在目录末尾追加勘误行。

PMD 过滤前后比较 PCA 或 f 统计、把明显位移当作现代样读段的警告，仍是可用于植物的检查，不是我们发明的数值门槛。提取和文库空白应当一起处理和测序。Latorre 等（2020，摘要）是植物古代 DNA 的分离、文库和生物信息学方案，不是被误当成题名的“专用 PCR 前实验室”论文。把酿酒实验室里的现代葡萄 DNA 当作主要风险，是现有 WORKFLOW 里的操作提醒，不是本次追加论文里的现成句子，不作发表比率来写。

论断—出处表见 [03_contamination.md](03_contamination.md)。
