# grapevine-adna

[English](README.md) | 中文

<!-- PROSE:INTRO -->
本仓库是 *Vitis* 古DNA研究的方法目录，涵盖取样、洁净实验室操作、DNA提取、文库构建、捕获或鸟枪法、测序、数据预处理、序列比对、损伤鉴定、污染评估、低覆盖度基因分型、测年，以及与现代葡萄联合开展的下游分析。与 [vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen) 的内容重叠在预期之内，予以保留。
<!-- /PROSE:INTRO -->

不包含未发表的基因型或私有地点坐标，也没有演示数据。

<!-- PROSE:STATUS -->
状态：本仓库已有捕获脚本（`scripts/`）和笔记（`notes/`）（于 2026-10-21 提交到 `main`；见第 14 节）。那些文件是捕获测试的生物信息流程，并不表示本仓库已经具备完整的、植物专用的湿实验方案。
<!-- /PROSE:STATUS -->

## 这不是

- 现代 167K 产品：[grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)
- 芯片设计：[grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip)
- 质体组装：[grapevine-plastid](https://github.com/Xuzhen-Li/grapevine-plastid)
- 理论汇编：[genomics-theory-book](https://github.com/Xuzhen-Li/genomics-theory-book)
- 现代群体遗传目录（有意重叠）：[vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen)

<!-- PROSE:CATALOG_NOTE -->
**2026-11-14 目录，第 3.2 版。** 体例与 vitis-popgen 一致：按分组归类、仅收录最新稳定版本、未经核对的项目标为 [待确认]（附加说明写在标记外面），流程见 [`docs/WORKFLOW.zh.md`](docs/WORKFLOW.zh.md)。本仓库已有 `scripts/` 和 `notes/` 下的文件（捕获测试的生物信息流程；见第 14 节）。
<!-- /PROSE:CATALOG_NOTE -->

---

## 目录

1. [取样与植物考古材料](#section-1) (10)
2. [洁净实验室与污染控制](#section-2) (8)
3. [提取方案](#section-3) (6)
4. [文库构建](#section-4) (7)
5. [捕获与鸟枪法](#section-5) (8)
6. [测序](#section-6) (1)
7. [预处理](#section-7) (4)
8. [比对](#section-8) (14)
9. [损伤鉴定](#section-9) (8)
10. [污染估计](#section-10) (5)
11. [低覆盖度基因分型与补全](#section-11) (4)
12. [测年](#section-12) (7)
13. [与现代样本的下游群体遗传分析](#section-13) (11)
14. [工作流与流程](#section-14) (4)
15. [植物与葡萄的特殊问题](#section-15) (6)
16. [关键研究、公开数据与模拟](#section-16) (7)
17. [同时收入 vitis-popgen 的工具](#section-17) (18)

本页共 128 条（其中工具 57 条；其余为流程、方案、文献、资源或想法）。表格形式见 [`ADDITIONS.tsv`](ADDITIONS.tsv) 和 [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv)。

<a id="section-1"></a>
## 1. 取样与植物考古材料

<!-- PROSE:SECTION:A01 -->
已发表的葡萄古DNA主要以种子为材料。一粒种子由多种组织构成：种皮为母本组织（基因型与母株一致，即对应栽培品种的克隆），胚为有性繁殖后代，胚乳在被子植物常见情况下为三倍体，包含两份母本基因组和一份父本基因组 [待确认]。Li 和 Berger 2012（doi:10.1111/j.1469-8137.2012.04182.x）是一篇关于胚乳发育的综述。考古葡萄籽中提取的 DNA 主要来源于哪种组织，目前尚未得到直接验证。胚由 L2（生殖细胞系）发育而来 [待确认]，而种皮 DNA 是否主要来源于 L1 仍为 [待确认]。周缘嵌合品种中的细胞层特异体细胞变异，不可作为判定“同一克隆”的关键位点（另见 vitis-popgen 中的 L1/L2 条目）。木材、残留物和标本馆材料属于次要材料来源，抑制剂和年代各不相同。
<!-- /PROSE:SECTION:A01 -->

**分组：**
- *Key grape seed studies (complementary)*：Cohen et al. 2023, Inanli et al. 2026, Noraz et al. 2026, Pérez-Jordà et al. 2026, Ramos-Madrigal et al. 2019, Cappellini et al. 2010 waterlogged grape seeds, Wales et al. 2016 grape paleogenomics。
- *Material types (complementary)*：Archaeological grape seeds (pips), Wood, fruit residues and herbarium sheets, Le et al. 2026 seed tissue ploidy。

- **Cohen et al. 2023**（文献）— 内盖夫高地荒漠葡萄种子的古DNA，显示古代晚期的一个酿酒谱系。 输入：n/a。输出：n/a。版本：n/a（Crossref title match, 2026-11-14 CST）。 [doi:10.1073/pnas.2213563120](https://doi.org/10.1073/pnas.2213563120) · [link](https://doi.org/10.1073/pnas.2213563120)  
  注：Includes radiocarbon dating of pips. Ancient reads: ENA PRJNA887039 (Ancient Negev grape DNA, 20 runs). Modern panels cited in the literature review: PRJNA887737, PRJNA647155.
- **Inanli et al. 2026**（文献）— 切塔穆拉井中的多项证据（古DNA、形态测量和近红外）。两口井中的 80 粒种子；超过四分之一属于一个延续数世纪的克隆，该主导无性系可能结白果；另有 2 粒符合深色果。 输入：n/a。输出：n/a。版本：n/a（Crossref title match, 2026-11-14 CST）。 [doi:10.1016/j.jas.2026.106605](https://doi.org/10.1016/j.jas.2026.106605) · [link](https://doi.org/10.1016/j.jas.2026.106605)  
  注：Data: ENA PRJEB89110 (title matches the paper; DS14). Wording follows the abstract: it does not say that most seeds were white-berry like.
- **Noraz et al. 2026**（文献）— 约 4000 年间的 49 粒考古种子，多数来自法国，也包括伊维萨岛及附近地区；无性系连续性包括一粒中世纪样本与黑皮诺一致，以及伊维萨岛一粒中世纪样本与 Folha de Figueira 一致。 输入：n/a。输出：n/a。版本：n/a（Crossref title match, 2026-11-14 CST）。 [doi:10.1038/s41467-026-70166-z](https://doi.org/10.1038/s41467-026-70166-z) · [link](https://doi.org/10.1038/s41467-026-70166-z)  
  注：Data: ENA PRJEB94459, titled ancient grapevine genomes from France and Ibiza (DS14). The paper focuses primarily on France; sample V156 is from medieval Ibiza (1027-1160 CE). Do not call the set '49 French pips'.
- **Pérez-Jordà et al. 2026**（文献）— 伊比利亚和撒丁岛的 28 粒种子；东方引入、与本地野生种杂交，以及赫本和帕萨巴伦西亚的长期无性保存。 输入：n/a。输出：n/a。版本：n/a（Crossref title match, 2026-11-14 CST）。 [doi:10.1016/j.cub.2026.08.039](https://doi.org/10.1016/j.cub.2026.08.039) · [link](https://doi.org/10.1016/j.cub.2026.08.039)  
  注：ENA accession for this paper was not confirmed in the literature review. PRJEB104344 ('Shotgun sequencing of two Iberian grapevine cultivar founders') is a candidate only and is not recorded here as the paper's dataset [待确认] (accession). Do not treat that project ID as verified.
- **Ramos-Madrigal et al. 2019**（文献）— 28 粒考古葡萄种子（法国），针对从 18K 葡萄芯片中选出的约 1 万个 SNP（10,207；Laucou 等 2018）做靶向富集；一粒中世纪种子与现用萨瓦涅白一致。 输入：n/a。输出：n/a。版本：n/a（Crossref title match, 2026-11-14 CST）。 [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://doi.org/10.1038/s41477-019-0437-5)  
  注：Data: PRJNA489970 and figshare 10.6084/m9.figshare.7610987 (DS14). The 10,207 SNP count is from Laucou et al. 2018 and from Cohen 2023 / Noraz 2026 descriptions of this design. Capture with myBaits is reported as myBaits protocol v3.0 in Cohen 2023's account of the same panel, not from the Ramos-Madrigal 2019 Methods (paywalled in the literature review) [待确认] (in the original Methods). The abstract says 28 archaeological grape seeds; the title and PRJNA489970 point to France, but the abstract does not itself say that every seed is French [待确认].
- **Cappellini et al. 2010 waterlogged grape seeds**（文献）— 饱水葡萄籽：DNA（5 个 SSR）、蛋白质和碳水化合物。5 个 SSR 不能指认品种，表面上的纯合也可能来自等位脱扣。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1007/s00114-009-0629-3](https://doi.org/10.1007/s00114-009-0629-3) · [link](https://doi.org/10.1007/s00114-009-0629-3)
- **Wales et al. 2016 grape paleogenomics**（文献）— 在考古葡萄籽上测试古基因组方法。文献核对读到了标题和 DOI，但没有读到摘要，所以这里的说明很有限 [待确认] (abstract)。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1016/j.jas.2016.05.014](https://doi.org/10.1016/j.jas.2016.05.014) · [link](https://doi.org/10.1016/j.jas.2016.05.014)
- **Archaeological grape seeds (pips)**（资源）— 已发表葡萄古DNA研究中最常用的材料：饱水或干燥的种子，有时可剖开一部分做碳十四。回收 DNA 的组织来源（种皮、胚还是胚乳）未经直接验证。 输入：excavated pips。输出：subsampled tissue。版本：n/a（literature below; DS14）。  
  注：Charred seeds usually yield little DNA. Combine with morphometrics (Terral school) when possible. Published grape pip studies that describe sampling used whole-seed grinding or drilling (Cohen 2023; Bolognesi 2025). No published grape pip study reviewed here reported allele-ratio evidence for the contributing tissue. See section 1 of the README and decision point 1 in docs/WORKFLOW.md.
- **Wood, fruit residues and herbarium sheets**（资源）— 次要材料：饱水木材、果实残体，以及标本馆的叶片或种子，抑制剂和损伤情况各不相同。 输入：wood, residues, herbarium。输出：subsampled tissue。版本：n/a（methods papers in section 3）。  
  注：Herbarium sheets often have a known collection year, which is a dating prior. Mercuric chloride treatments damage DNA.
- **Le et al. 2026 seed tissue ploidy**（文献）— 比较了标本馆材料中胚和叶片的 DNA；引言概括了种皮（2n，母本）、胚乳（3n）和胚（2n）的倍性。该研究材料是稻和野生大麦，不是葡萄，此处只引用这一组织遗传学背景。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1111/1755-0998.70210](https://doi.org/10.1111/1755-0998.70210) · [link](https://doi.org/10.1111/1755-0998.70210)

<a id="section-2"></a>
## 2. 洁净实验室与污染控制

<!-- PROSE:SECTION:A02 -->
设立独立的扩增前实验空间、单向工作流，并对空白对照进行测序。葡萄酒或葡萄实验室是现代品种 DNA 污染的高风险来源。
<!-- /PROSE:SECTION:A02 -->

**分组：**
- *Lab practice (in order)*：Dedicated pre-PCR aDNA laboratory, Extraction and library blanks。
- *Key lab-practice references (complementary)*：Cooper and Poinar 2000 authenticity criteria, Gilbert et al. 2005 authenticity critique, Llamas et al. 2017 contamination control, Fulton and Shapiro 2019 lab setup, Knapp et al. 2012 lab setup, Korlević et al. 2015 bleach pretreatment。

- **Dedicated pre-PCR aDNA laboratory**（方案）— 提取和建库都在独立的扩增前空间进行，配防护、漂白或等效清洁，以及单向工作流。 输入：samples。输出：controlled extracts。版本：n/a（standard aDNA practice, summarised in Latorre et al. 2020）。 [doi:10.1002/cppb.20121](https://doi.org/10.1002/cppb.20121) · [link](https://doi.org/10.1002/cppb.20121)  
  注：DOI is Latorre et al. 2020, which states these requirements for plant aDNA.
- **Extraction and library blanks**（方案）— 每批都做提取空白和文库空白并测序。葡萄酒实验室是现代葡萄 DNA 的高风险环境。 输入：blank reactions。输出：blank libraries, contamination metrics。版本：n/a（standard aDNA practice）。  
  注：Modern cultivar DNA in a viticulture institute can look like a true ancient match. Treat unexpected clone matches with extra contamination checks.
- **Cooper and Poinar 2000 authenticity criteria**（文献）— 古DNA工作的经典真实性标准。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1126/science.289.5482.1139b](https://doi.org/10.1126/science.289.5482.1139b) · [link](https://doi.org/10.1126/science.289.5482.1139b)
- **Gilbert et al. 2005 authenticity critique**（文献）— 对古DNA真实性标准的批评和修订。输入：n/a。输出：n/a。版本：n/a（Crossref 核对，2026-11-14 CST）。[doi:10.1016/j.tree.2005.07.005](https://doi.org/10.1016/j.tree.2005.07.005) · [link](https://doi.org/10.1016/j.tree.2005.07.005)
- **Llamas et al. 2017 contamination control**（文献）— 从田野到实验室的污染控制，原文面向人类古DNA，但实验室规则仍可借鉴。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1080/20548923.2016.1258824](https://doi.org/10.1080/20548923.2016.1258824) · [link](https://doi.org/10.1080/20548923.2016.1258824)
- **Fulton and Shapiro 2019 lab setup**（文献）— 如何建立和运行专门的古DNA洁净实验室。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1007/978-1-4939-9176-1_1](https://doi.org/10.1007/978-1-4939-9176-1_1) · [link](https://doi.org/10.1007/978-1-4939-9176-1_1)
- **Knapp et al. 2012 lab setup**（文献）— 古DNA实验室的实际设计和流程。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1016/j.aanat.2011.03.008](https://doi.org/10.1016/j.aanat.2011.03.008) · [link](https://doi.org/10.1016/j.aanat.2011.03.008)
- **Korlević et al. 2015 bleach pretreatment**（文献）— 用漂白和预消化减少表面污染；在骨骼上测试，用于植物还需要检验。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.2144/000114320](https://doi.org/10.2144/000114320) · [link](https://doi.org/10.2144/000114320)

<a id="section-3"></a>
## 3. 提取方案

<!-- PROSE:SECTION:A03 -->
较古老或考古植物遗存用 PTB-DTT 加硅胶；并与 2025 年葡萄种子的 S-PDE 方案比较，而不是盲目只用一种方法。
<!-- /PROSE:SECTION:A03 -->

**分组：**
- *Inhibitor-rich grape pips (alternatives)*：S-PDE extraction on archaeological grape pips (Bolognesi et al. 2025)。
- *Silica and cross-link methods (alternatives)*：Dabney silica binding for ultra-short DNA, PTB-DTT plant extraction (Gutaker / Latorre), Wales and Kistler plant-remains extraction。
- *Key extraction references (complementary)*：Wales et al. 2014 archaeobotanical extraction, Rohland et al. 2018 extraction protocol。

- **S-PDE extraction on archaeological grape pips (Bolognesi et al. 2025)**（方案）— 针对土壤抑制剂优化的提取，再加古DNA硅胶结合，用于古代葡萄种子；在两个考古背景中建库成功率高于 CTAB 或 DNeasy。 输入：archaeological grape pips。输出：libraries。版本：2025 paper（Crossref title match, 2026-11-14 CST）。 [doi:10.1038/s41598-025-21743-7](https://doi.org/10.1038/s41598-025-21743-7) · [link](https://doi.org/10.1038/s41598-025-21743-7)  
  注：The paper supports a higher library-success rate for S-PDE than for CTAB or DNeasy in two archaeological contexts, with sample-size limits: the library comparison used n = 8 for CTAB and DNeasy and n = 30 for S-PDE (Fig. 2 legend). The fourth method, phenol-chloroform, yielded no detectable DNA in any of eight extracts in their hands, so it was not a direct comparison with earlier phenol-chloroform grape-pip protocols that had worked elsewhere.
- **Dabney silica binding for ultra-short DNA**（方案）— 能保住极短片段的硅胶结合缓冲液，被广泛用于植物遗存。 输入：lysate。输出：short-fragment DNA extract。版本：2013 paper（Crossref title match, 2026-11-14 CST）。 [doi:10.1073/pnas.1314445110](https://doi.org/10.1073/pnas.1314445110) · [link](https://doi.org/10.1073/pnas.1314445110)  
  注：The paper is a cave bear mitogenome demonstration; the binding buffer is the widely used method.
- **PTB-DTT plant extraction (Gutaker / Latorre)**（方案）— PTB 和 DTT 把交联中的 DNA 释放出来，再结合硅胶。Latorre 等 2020 建议用于较老的标本和考古遗存。 输入：herbarium or archaeological tissue。输出：extract。版本：Gutaker 2017; Latorre 2020（Crossref title match, 2026-11-14 CST）。 [doi:10.2144/000114517](https://doi.org/10.2144/000114517) · [link](https://doi.org/10.2144/000114517)  
  注：Gutaker et al. 2017 doi:10.2144/000114517. Protocol compilation: Latorre et al. 2020 doi:10.1002/cppb.20121. Marinček et al. 2022 (doi:10.1002/aps3.11477) found PTB-DTT better than a standard kit for old herbarium, while a kit may suffice for young sheets.
- **Wales and Kistler plant-remains extraction**（方案）— 《Methods in Molecular Biology》中关于从植物遗存提取古DNA的章节，包括 SDS 与 CTAB 的选择。 输入：plant remains。输出：extract。版本：2019 chapter（Crossref title match, 2026-11-14 CST）。 [doi:10.1007/978-1-4939-9176-1_6](https://doi.org/10.1007/978-1-4939-9176-1_6) · [link](https://doi.org/10.1007/978-1-4939-9176-1_6)  
  注：更早的 Kistler 2012 书章：doi:10.1007/978-1-61779-516-9_10。Wales 等 2014（doi:10.1371/journal.pone.0086827）另有独立条目；该文报告，在未炭化（主要为干燥）的植物考古遗存上，SDS 往往优于 CTAB；炭化材料未经测试。
- **Wales et al. 2014 archaeobotanical extraction**（文献）— 在未炭化的植物考古残留（包括葡萄籽）上比较提取方法，Cohen 等 2023 曾使用。Bolognesi 2025 转述，该文中 SDS/蛋白酶 K/DTT 加酚氯仿的效果更好。2014 年的材料主要是干燥而非炭化的，不能直接外推到炭化籽。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1371/journal.pone.0086827](https://doi.org/10.1371/journal.pone.0086827) · [link](https://doi.org/10.1371/journal.pone.0086827)
- **Rohland et al. 2018 extraction protocol**（文献）— 更新的硅胶提取方案（骨、牙、沉积物），是许多后来植物适配方案的基础。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1038/s41596-018-0050-5](https://doi.org/10.1038/s41596-018-0050-5) · [link](https://doi.org/10.1038/s41596-018-0050-5)

<a id="section-4"></a>
## 4. 文库构建

<!-- PROSE:SECTION:A04 -->
在双链或单链文库之间作出选择，并事先登记 UDG 处理方式（不处理、半处理或全处理）。预期的损伤模式取决于上述选择（见第 9 节）。完全 UDG 处理无法去除植物 CG、CHG、CHH 位点上甲基化胞嘧啶脱氨生成的胸腺嘧啶（T）。
<!-- /PROSE:SECTION:A04 -->

**分组：**
- *Damage treatment (alternatives)*：Partial UDG (UDG-half) treatment。
- *Double-stranded libraries (alternatives)*：Meyer and Kircher double-stranded library。
- *Single-stranded libraries (alternatives)*：Gansauge single-stranded library (ssDNA2 and later automated versions), Santa Cruz reaction (SCR)。
- *Key damage-treatment references (complementary)*：Briggs et al. 2010 USER/UDG。
- *Key library references (complementary)*：Carøe et al. 2018 single-tube library, Wales et al. 2015 ss versus ds libraries。

- **Partial UDG (UDG-half) treatment**（方案）— 去掉大部分内部尿嘧啶，但保留末端损伤以便鉴定。 输入：extract or pre-library DNA。输出：UDG-half DNA。版本：Rohland et al. 2015（Crossref title match, 2026-11-14 CST）。 [doi:10.1098/rstb.2013.0624](https://doi.org/10.1098/rstb.2013.0624) · [link](https://doi.org/10.1098/rstb.2013.0624)  
  注：Choose UDG-half, full UDG, or no UDG in advance. No-UDG keeps more damage for authentication but complicates transition sites. Full UDG is cleaner for genotyping but weaker for damage evidence.
- **Meyer and Kircher double-stranded library**（方案）— 经典的平末端双链古DNA文库，可用单端或双端标签。 输入：extract。输出：ds library。版本：2010（Crossref title match, 2026-11-14 CST）。 [doi:10.1101/pdb.prot5448](https://doi.org/10.1101/pdb.prot5448) · [link](https://doi.org/10.1101/pdb.prot5448)  
  注：Pair with unique dual indexes (Kircher et al. 2012, doi:10.1093/nar/gkr771). The existing repo notes describe a dsDNA batch.
- **Gansauge single-stranded library (ssDNA2 and later automated versions)**（方案）— 单链文库能回收带单链断裂或末端阻断的分子，内源含量低时往往更好。 输入：extract。输出：ss library。版本：2013 / 2017 / 2020（Crossref title matches, 2026-11-14 CST）。 [doi:10.1038/s41596-020-0338-0](https://doi.org/10.1038/s41596-020-0338-0) · [link](https://doi.org/10.1038/s41596-020-0338-0)  
  注：2013 Nature Protocols doi:10.1038/nprot.2013.038; 2017 NAR doi:10.1093/nar/gkx033; 2020 Nat Protoc doi:10.1038/s41596-020-0338-0.
- **Santa Cruz reaction (SCR)**（方案）— 更快的单链建库方法，古DNA实验室常用；另有 2025 年 protocols.io 更新。 输入：extract。输出：ss library。版本：Kapp 2021（Crossref title match, 2026-11-14 CST）。 [doi:10.1093/jhered/esab012](https://doi.org/10.1093/jhered/esab012) · [link](https://doi.org/10.1093/jhered/esab012)  
  注：Kapp et al. 2021. Protocol updates on protocols.io were seen in search results but not used as a substitute for the paper.
- **Briggs et al. 2010 USER/UDG**（文献）— 对古DNA文库做全 UDG 加核酸内切酶 VIII（USER）处理。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1093/nar/gkp1163](https://doi.org/10.1093/nar/gkp1163) · [link](https://doi.org/10.1093/nar/gkp1163)
- **Carøe et al. 2018 single-tube library**（文献）— 平末端单管（BEST）双链文库；Cohen 等 2023 的部分文库引用了这一方法。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1111/2041-210x.12871](https://doi.org/10.1111/2041-210x.12871) · [link](https://doi.org/10.1111/2041-210x.12871)
- **Wales et al. 2015 ss versus ds libraries**（文献）— 在古DNA提取物上比较单链和双链建库。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.2144/000114364](https://doi.org/10.2144/000114364) · [link](https://doi.org/10.2144/000114364)

<a id="section-5"></a>
## 5. 捕获与鸟枪法

<!-- PROSE:SECTION:A05 -->
浅层鸟枪法测序可用于筛查文库；随后可通过更深度的鸟枪法或溶液内靶向捕获提升覆盖度。已发表的葡萄籽捕获研究使用的是从 18K 葡萄芯片中筛选出的约 1 万个 SNP（10,207 个；Laucou 等 2018），而非全部 18k 位点。细胞器读段在属一级有帮助，相关局限性见质体条目。
<!-- /PROSE:SECTION:A05 -->

**分组：**
- *Strategy (alternatives)*：In-solution target enrichment (myBaits / similar), Shallow shotgun screening then deeper shotgun。
- *Strategy (complementary)*：Plastid, mitochondrion and rDNA as authentication and species ID, Organelle-to-nuclear read ratio (idea)。
- *Key capture references (complementary)*：Maricic et al. 2010 homemade capture, Carpenter et al. 2013 whole-genome capture, Cruz-Dávalos et al. 2017 capture conditions, Laucou et al. 2018 10K grape SNP panel。

- **In-solution target enrichment (myBaits / similar)**（方案）— 针对葡萄 SNP 面板的溶液内捕获。Ramos-Madrigal 及后续葡萄论文用的是从 18K 芯片中选出的约 1 万个 SNP（10,207；Laucou 等 2018）。 输入：libraries, bait set。输出：enriched libraries。版本：[待确认] kit version（used in Ramos-Madrigal 2019 and later grape studies; kit version not pinned here）。 [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://doi.org/10.1038/s41477-019-0437-5)  
  注：Do not call the capture panel an 18k-site panel. The 10,207 figure is from Laucou et al. 2018 (10.1371/journal.pone.0192540). Cohen 2023 reports capturing this set with the myBaits protocol version 3.0; that kit version is Cohen's description [待确认] (against Ramos-Madrigal 2019 Methods). Kit version in general remains [待确认].
- **Shallow shotgun screening then deeper shotgun**（想法）— 先浅测筛选文库，再只对内源含量可用、损伤真实的文库加深测序。 输入：libraries。输出：screening metrics, deeper data。版本：n/a（standard palaeogenomics practice）。  
  注：Good when fragments are very short or bait design would miss variation.
- **Plastid, mitochondrion and rDNA as authentication and species ID**（想法）— 细胞器和核糖体 DNA 读段可用于鉴定和属一级的物种判断。葡萄质体基本上是母系遗传，但葡萄属各物种之间序列差异很小，还可能发生叶绿体捕获，所以质体数据不足以做属内种或品种鉴定。类似异质性的信号，往往来自核基因组里的质体或线粒体插入（NUPT、NUMT），以及线粒体基因组里的质体来源片段。 输入：libraries。输出：organelle coverage, species ID。版本：n/a（standard plant aDNA practice）。  
  注：Use organelle-to-nuclear read ratios only as a secondary preservation or authenticity indicator, and compete-map to reduce NUPT/NUMT confusion. See also grapevine-plastid.
- **Organelle-to-nuclear read ratio (idea)**（想法）— 把质体/线粒体与核读段的比例和现代葡萄基线比较，作为保存状况和真实性的辅助指标。核基因组里的质体插入（NUPT）会干扰，需要竞争性比对。 输入：BAM。输出：organelle-to-nuclear ratio。版本：n/a（methods review, 2026-11-14 CST）。
- **Maricic et al. 2010 homemade capture**（文献）— 用于多重古DNA文库的低成本自制捕获探针。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1371/journal.pone.0014004](https://doi.org/10.1371/journal.pone.0014004) · [link](https://doi.org/10.1371/journal.pone.0014004)
- **Carpenter et al. 2013 whole-genome capture**（文献）— 全基因组溶液内捕获（WISC），用于提高内源含量。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1016/j.ajhg.2013.10.002](https://doi.org/10.1016/j.ajhg.2013.10.002) · [link](https://doi.org/10.1016/j.ajhg.2013.10.002)
- **Cruz-Dávalos et al. 2017 capture conditions**（文献）— 针对溶液内古DNA捕获条件（温度、探针、轮次）的测试。输入：n/a。输出：n/a。版本：n/a（Crossref 核对，2026-11-14 CST）。[doi:10.1111/1755-0998.12595](https://doi.org/10.1111/1755-0998.12595) · [link](https://doi.org/10.1111/1755-0998.12595)
- **Laucou et al. 2018 10K grape SNP panel**（文献）— 用于古籽捕获的葡萄 10K SNP 集（783 个基因型，从 18K 芯片中选出 10,207 个 SNP）。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1371/journal.pone.0192540](https://doi.org/10.1371/journal.pone.0192540) · [link](https://doi.org/10.1371/journal.pone.0192540)

<a id="section-6"></a>
## 6. 测序

<!-- PROSE:SECTION:A06 -->
采用唯一双端标签和短插入片段双端测序。记录实际使用的仪器，切勿虚构默认机型。
<!-- /PROSE:SECTION:A06 -->

**分组：**
- *Sequencing practice (in order)*：Unique dual indexing and short-insert PE sequencing。

- **Unique dual indexing and short-insert PE sequencing**（方案）— 使用唯一双端标签以减少 index hopping。双端 75 或 100 bp 通常覆盖典型古DNA插入长度。 输入：indexed libraries。输出：FASTQ。版本：Kircher et al. 2012 plus current Illumina practice（Kircher DOI verified; instrument versions not pinned）。 [doi:10.1093/nar/gkr771](https://doi.org/10.1093/nar/gkr771) · [link](https://doi.org/10.1093/nar/gkr771)  
  注：Demultiplex conservatively. Do not invent a preferred instrument model; record the one actually used.

<a id="section-7"></a>
## 7. 预处理

<!-- PROSE:SECTION:A07 -->
短插入片段的接头修剪与序列合并。合并后读段的默认最小长度设为 30 bp，原因在于葡萄基因组重复序列多且杂合度高；25 bp 仅用于敏感性分析。
<!-- /PROSE:SECTION:A07 -->

**分组：**
- *Adapter trimming and collapsing (alternatives)*：AdapterRemoval, Cutadapt, leeHom。
- *Complexity and QC (complementary)*：preseq。

- **AdapterRemoval**（工具）— 修剪接头、合并重叠双端，并设最小长度。本仓库现有笔记中的默认工具。 输入：paired FASTQ。输出：collapsed and singleton FASTQ。版本：3.0.2（GitHub MikkelSchubert/adapterremoval + Bioconda, 2026-11-14 CST (release 2026-08-20)）。 [doi:10.1186/s13104-016-1900-2](https://doi.org/10.1186/s13104-016-1900-2) · [link](https://github.com/MikkelSchubert/adapterremoval)  
  注：The verified DOI is AdapterRemoval v2 (Schubert 2016). Newest software is 3.0.2. Existing notes use --trimqualities --minquality 2 --trimns --minlength 25 --collapse (dsDNA batch --minlength 30). Re-check flags if you move from v2 to v3. The catalogue version is the newest tool line (v2 paper already cited). The first AdapterRemoval paper is Lindgreen 2012, 10.1186/1756-0500-5-337, and is not a second tool entry.
- **Cutadapt**（工具）— 通用接头修剪器；可用，但古DNA流程更常用 AdapterRemoval 或 leeHom，因为需要合并双端。 输入：FASTQ。输出：trimmed FASTQ。版本：5.2（Bioconda/PyPI cutadapt 5.2; GitHub tags are stale (v4.0)）。 [link](https://github.com/marcelm/cutadapt)
- **leeHom**（工具）— 贝叶斯接头修剪与合并，部分古DNA流程中的备选。 输入：paired FASTQ。输出：merged FASTQ。版本：1.2.18（GitHub grenaud/leeHom + Bioconda, 2026-11-14 CST）。 [doi:10.1093/nar/gku699](https://doi.org/10.1093/nar/gku699) · [link](https://github.com/grenaud/leeHom)  
  注：Method paper: 10.1093/nar/gku699 (Crossref-verified in the literature review).
- **preseq**（工具）— 文库复杂度曲线，nf-core/eager 用它判断是否值得加深测序。 输入：BAM or reads。输出：complexity curve。版本：3.2.0（GitHub smithlabcode/preseq + Bioconda, 2026-11-14 CST）。 [link](https://github.com/smithlabcode/preseq)

<a id="section-8"></a>
## 8. 比对

<!-- PROSE:SECTION:A08 -->
默认比对工具为关闭 seed 的 bwa aln。各项参数及其出处需分开注明，仓库现有脚本中的参数须逐字引用。对于合并后的读段，默认使用 DeDup 去除重复。Schubert 2012 与古人类常用比对参数的区别见流程页。
<!-- /PROSE:SECTION:A08 -->

**分组：**
- *Competitive mapping and composition (complementary)*：FastQ Screen, Kraken2, MALT, HOPS。
- *Graph mapping for ancient seeds (complementary)*：vg Giraffe。
- *Post-mapping filters (in order)*：samtools + Picard MarkDuplicates or DeDup。
- *Short aDNA alignment (alternatives)*：CircularMapper, bowtie2。
- *Short aDNA alignment (default route)*：bwa aln (disabled seeding)。
- *Key mapping references (complementary)*：Oliva et al. 2021 mapping benchmark, Schubert et al. 2012 bwa aln parameters。
- *Reference bias (complementary)*：Dolenz et al. 2024 reference bias, Günther and Nettelblad 2019 reference bias, Martiniano et al. 2020 graph mapping。

- **FastQ Screen**（工具）— 把读段放到葡萄、人类、微生物和其他植物参考上筛查，以便发现拿错和污染。 输入：FASTQ, multiple references。输出：composition tables。版本：0.16.0（GitHub StevenWingett/FastQ-Screen + Bioconda, 2026-11-14 CST）。 [link](https://github.com/StevenWingett/FastQ-Screen)  
  注：Competitive mapping against several Vitis references or a graph is the natural next step (project 20).
- **Kraken2**（工具）— 对未比对或全部读段做分类组成分析。 输入：FASTQ or unmapped BAM。输出：taxonomic report。版本：2.17.2（Bioconda kraken2 2.17.2 (latest stable); GitHub also has v2.18.0-RC2, not used here）。 [link](https://github.com/DerrickWood/kraken2)  
  注：A 2.18.0 release candidate exists (2026-11-06) and is not used as the catalog version.
- **MALT**（工具）— 基于比对的宏基因组分箱，用于 nf-core/eager。 输入：reads, MALT database。输出：rma, taxon tables。版本：0.5.2（GitHub husonlab/malt + Bioconda, 2026-11-14 CST）。 [link](https://github.com/husonlab/malt)
- **HOPS**（工具）— MALT 加 MaltExtract，带损伤鉴定的微生物筛查。用于葡萄种子时，只做微生物和植物病原组成分析，不能用来鉴定葡萄内源 DNA 的真实性。 输入：reads, MALT database。输出：taxon list and damage statistics。版本：0.35（GitHub rhuebler/HOPS release 0.35, checked 2026-11-14 CST; Bioconda reported in the methods review）。 [doi:10.1186/s13059-019-1903-0](https://doi.org/10.1186/s13059-019-1903-0) · [link](https://github.com/rhuebler/HOPS)
- **vg Giraffe**（工具）— 把古代读段比对到葡萄泛基因组图上，并与线性比对的等位基因平衡做比较（项目 20）。 输入：FASTQ, graph。输出：GAM/BAM, VCF。版本：1.78.0（see vitis-popgen section 11; also AM17）。 [link](https://github.com/vgteam/vg)  
  注：Test on downsampled modern grapes before ancient seeds.
- **samtools + Picard MarkDuplicates or DeDup**（工具）— 比对后的 BAM 过滤。对合并后的单端古DNA读段，默认用 DeDup 去重复，因为它同时使用两端坐标；Picard MarkDuplicates 只看 5 端坐标，会多删。MarkDuplicates 可作对照。 输入：SAM/BAM。输出：deduplicated BAM, flagstat。版本：samtools 1.25; Picard 3.5.0; DeDup 0.12.9（versions checked 2026-11-14 CST）。 [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008) · [link](https://github.com/samtools/samtools)  
  注：合并读段默认使用 DeDup；若改用其他工具需说明原因。记录版本：samtools 1.25；Picard 3.5.0；DeDup 0.12.9。
- **CircularMapper**（工具）— 改善对环状细胞器参考（质体、线粒体）的比对。 输入：FASTQ, circular FASTA。输出：BAM。版本：1.93.5（GitHub apeltzer/CircularMapper + Bioconda, 2026-11-14 CST）。 [link](https://github.com/apeltzer/CircularMapper)  
  注：Complementary to nuclear bwa aln, not a replacement.
- **bowtie2**（工具）— nf-core/eager 提供的备选局部比对器。 输入：FASTQ, reference。输出：BAM。版本：2.5.5（GitHub BenLangmead/bowtie2 + Bioconda, 2026-11-14 CST）。 [link](https://github.com/BenLangmead/bowtie2)  
  注：Use only if a comparison against bwa aln is pre-registered. Not the default in the existing repo scripts.
- **bwa aln (disabled seeding)**（工具）— 损伤古DNA短读的默认比对器。各参数和出处要分开写，不要把仓库脚本里的值和文献参数混在一起。 输入：collapsed FASTQ, reference FASTA。输出：BAM。版本：0.7.19（GitHub lh3/bwa + Bioconda, 2026-11-14 CST; parameter sources listed in the note）。 [doi:10.1186/1471-2164-13-178](https://doi.org/10.1186/1471-2164-13-178) · [link](https://github.com/lh3/bwa)  
  注：Parameter sources, checked against Schubert et al. 2012 (10.1186/1471-2164-13-178): `-l 1024` disables the seed on Illumina data (Schubert 2012); Schubert kept the default `-n` 0.04 for Illumina. The Helicos setting in that paper is `-l 1024 -i 0 -o 2 -n 0.03`, not the Illumina setting. The combination `-n 0.01 -o 2` is common in ancient human studies (often with `-l 16500`) and is cited by Dolenz et al. 2024 as coming from Green et al. 2010; the original source remains [待确认]. For a benchmark of parameterised BWA-aln, BWA-mem and NovoAlign on simulated human reads, see the Oliva et al. 2021 row; that paper does not establish a single preferred aligner.
- **Oliva et al. 2021 mapping benchmark**（文献）— 在模拟人类读段上比较了 30 种古DNA比对策略：特定参数下的 BWA-aln、BWA-mem 和 NovoAlign 都能达到高精度和低参考偏倚，MAPQ 过滤后更好；无偏的 NovoAlign 需要 IUPAC 参考基因组。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature and methods reviews, 2026-11-14 CST）。 [doi:10.1093/bib/bbab076](https://doi.org/10.1093/bib/bbab076) · [link](https://doi.org/10.1093/bib/bbab076)
- **Schubert et al. 2012 bwa aln parameters**（文献）— Illumina 数据上用 `-l 1024` 关闭 seed 的出处。Helicos 的命令行不同。该文证明了什么、没证明什么，见 bwa aln 条目的备注。 输入：n/a。输出：n/a。版本：n/a（already the DOI on the bwa aln row; restated as a source note）。 [doi:10.1186/1471-2164-13-178](https://doi.org/10.1186/1471-2164-13-178) · [link](https://doi.org/10.1186/1471-2164-13-178)
- **Dolenz et al. 2024 reference bias**（文献）— 评估不同比对器和 MAPQ 阈值造成的古DNA参考偏倚，测试数据包含植物（玉米）例子。把古籽比对到 PN40024 时可参考。 输入：n/a。输出：n/a。版本：n/a（EuropePMC PMID 38960861 and Crossref, 2026-11-14 CST）。 [doi:10.1093/bioinformatics/btae436](https://doi.org/10.1093/bioinformatics/btae436) · [link](https://doi.org/10.1093/bioinformatics/btae436)  
  注：Title: Unravelling reference bias in ancient DNA datasets. Crossref issued 2024-07-01.
- **Günther and Nettelblad 2019 reference bias**（文献）— 低覆盖古DNA中的参考偏倚，与把古籽比对到 PN40024 有关。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1371/journal.pgen.1008302](https://doi.org/10.1371/journal.pgen.1008302) · [link](https://doi.org/10.1371/journal.pgen.1008302)
- **Martiniano et al. 2020 graph mapping**（文献）— 用图基因组比对降低古DNA中的参考偏倚。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1186/s13059-020-02160-7](https://doi.org/10.1186/s13059-020-02160-7) · [link](https://doi.org/10.1186/s13059-020-02160-7)

<a id="section-9"></a>
## 9. 损伤鉴定

<!-- PROSE:SECTION:A09 -->
损伤图谱既是鉴定步骤，也决定了基因型检测前如何处理残留损伤。首先根据文库类型和 UDG 处理方式设定预期模式：双链文库通常表现为 5 端 C 到 T、3 端 G 到 A 替换；单链文库两端均表现为 C 到 T；UDG-half 处理后，损伤基本留在末端 1 到 2 个碱基。
<!-- /PROSE:SECTION:A09 -->

**分组：**
- *Damage profiles (alternatives)*：DamageProfiler, mapDamage2。
- *Damage-read filters (complementary)*：PMDtools, pyDamage。
- *Damage-read handling (in order, after profiling)*：bamUtil trimBam, Damage pattern by library type and UDG (idea)。
- *Key damage-profile references (complementary)*：Briggs et al. 2007 damage pattern, Sawyer et al. 2012 damage versus age。

- **DamageProfiler**（工具）— 更快的损伤模式计算，nf-core/eager 中相对 mapDamage2 的备选。 输入：BAM, reference。输出：damage plots, tables。版本：1.1（GitHub Integrative-Transcriptomics/DamageProfiler + Bioconda, 2026-11-14 CST）。 [doi:10.1093/bioinformatics/btab190](https://doi.org/10.1093/bioinformatics/btab190) · [link](https://github.com/Integrative-Transcriptomics/DamageProfiler)  
  注：Last tagged release remains 1.1 (2020). Still the current Bioconda version.
- **mapDamage2**（工具）— AM17 和 scripts/run_mapdamage.sh 中的默认损伤与片段长度分析。 输入：BAM, reference。输出：misincorporation plots, optional rescaled BAM。版本：2.2.3（GitHub ginolhac/mapDamage + Bioconda, 2026-11-14 CST (also AM17)）。 [doi:10.1093/bioinformatics/btt193](https://doi.org/10.1093/bioinformatics/btt193) · [link](https://github.com/ginolhac/mapDamage)  
  注：Existing wrapper: mapDamage -i BAM -r REF -d OUT --merge-reference-sequences. Use this, not a later untested flag set, unless you re-validate. Cite with the original mapDamage paper (Ginolhac et al. 2011, 10.1093/bioinformatics/btr347) when describing damage plots. --rescale can downweight likely damaged bases as an alternative to hard trimming; compare the two on downsampled data.
- **PMDtools**（工具）— 按死后损伤给读段打分并过滤，把内源读段和更像现代的读段分开。 输入：BAM。输出：PMD-filtered BAM, scores。版本：0.60（GitHub pontussk/PMDtools + Bioconda, 2026-11-14 CST）。 [doi:10.1073/pnas.1318934111](https://doi.org/10.1073/pnas.1318934111) · [link](https://github.com/pontussk/PMDtools)  
  注：Skoglund et al. 2014 DOI verified.
- **pyDamage**（工具）— 按条目估计损伤，适合参考很多的情况（宏基因组或竞争性比对）。 输入：BAM。输出：per-contig damage。版本：1.0（GitHub maxibor/pydamage + Bioconda/PyPI, 2026-11-14 CST）。 [doi:10.7717/peerj.11845](https://doi.org/10.7717/peerj.11845) · [link](https://github.com/maxibor/pydamage)
- **bamUtil trimBam**（工具）— 按文库类型和 UDG 处理方式修剪读段两端 N 个碱基，例如 UDG-half 后每端修 2 nt，再做伪单倍型调用。 输入：BAM。输出：trimmed BAM。版本：v1.0.15（GitHub statgen/bamUtil release v1.0.15, checked 2026-11-14 CST）。 [link](https://github.com/statgen/bamUtil)  
  注：Method DOI [待确认]. This is the default terminal-trim tool named in the methods review.
- **Damage pattern by library type and UDG (idea)**（想法）— 判读损伤图之前，先按文库类型设定预期：双链文库是 5 端 C 到 T、3 端 G 到 A；单链文库两端都是 C 到 T；UDG-half 后损伤基本留在末端 1 到 2 个碱基；全 UDG 可去掉大部分这类损伤，但植物甲基化胞嘧啶（CG/CHG/CHH）脱氨生成的 T 去不掉。 输入：damage profiles。输出：trim or filter plan。版本：n/a（genetics and methods reviews, 2026-11-14 CST）。
- **Briggs et al. 2007 damage pattern**（文献）— 定义了用于鉴定的末端 C 到 T 损伤模式。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1073/pnas.0704665104](https://doi.org/10.1073/pnas.0704665104) · [link](https://doi.org/10.1073/pnas.0704665104)
- **Sawyer et al. 2012 damage versus age**（文献）— 损伤和片段长度与年代的关系；损伤不是简单的分子钟。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1371/journal.pone.0034131](https://doi.org/10.1371/journal.pone.0034131) · [link](https://doi.org/10.1371/journal.pone.0034131)

<a id="section-10"></a>
## 10. 污染估计

<!-- PROSE:SECTION:A10 -->
优先采用适用于植物的污染评估方法：空白对照测序、组成分析，以及对比 PMD 过滤前后的分析结果。AuthentiCT 仅适用于单链文库。hapCon 及其他依赖男性 X 染色体的方法不适用于葡萄。古葡萄籽中异常的杂合度或等位基因比例，也可能源于母本与胚或含胚乳的组织混合，不一定是污染。仅凭等位基因比例既无法区分组织混合与现代污染，也无法判断哪一组分来自母本。区分组织混合与现代污染的主要依据是损伤分层读段与片段长度分布；亲子关系检验仅能排除无关的污染源（详见第 13 节的构想与流程页）。
<!-- /PROSE:SECTION:A10 -->

**分组：**
- *Model-based tools with caveats (alternatives)*：AuthentiCT, hapCon, schmutzi。
- *Plant-appropriate checks (complementary)*：Blanks, species composition and excess heterozygosity, PMD-filter drift check (idea)。

- **AuthentiCT**（工具）— 用损伤模式估计现代污染。只要有参考基因组就可用于各物种，但仅限单链文库。 输入：BAM or damage patterns。输出：contamination fraction。版本：v1.0.1（GitHub StephanePeyregne/AuthentiCT tag and release v1.0.1 (2023-03-10), checked 2026-11-14 CST）。 [doi:10.1186/s13059-020-02123-y](https://doi.org/10.1186/s13059-020-02123-y) · [link](https://github.com/StephanePeyregne/AuthentiCT)  
  注：Single-stranded libraries only. Do not use it on UDG-treated data or after PMD filtering (official README). The repository exists (https://github.com/StephanePeyregne/AuthentiCT); it is not a 404. Do not run it on the default double-stranded branch of this workflow.
- **hapCon**（工具）— 利用男性 X 染色体估计人类污染的工具。列在这里只是为了防止误用，不适用于葡萄。 输入：haploid calls, reference panel。输出：contamination estimate。版本：[待确认]（Huang et al. 2022 paper verified; software tag not checked）。 [doi:10.1093/bioinformatics/btac390](https://doi.org/10.1093/bioinformatics/btac390) · [link](https://github.com/hringbauer/hapROH)  
  注：hapCon requires a hemizygous male X chromosome (Huang and Ringbauer 2022). Grape has no such chromosome, so this is not a tool that can be tested into applicability. Keep the entry as a warning, like schmutzi.
- **schmutzi**（工具）— 为人类设计的线粒体污染估计。不是葡萄核基因组污染工具。 输入：mt BAM。输出：contamination estimate。版本：1.5.7（GitHub grenaud/schmutzi + Bioconda, 2026-11-14 CST）。 [doi:10.1186/s13059-015-0776-0](https://doi.org/10.1186/s13059-015-0776-0) · [link](https://github.com/grenaud/schmutzi)  
  注：Listed so that it is not used by mistake for nuclear grape data. Written for human mtDNA; grape use would need testing. Listed to prevent uncritical reuse. DOI 10.1186/s13059-015-0776-0.
- **Blanks, species composition and excess heterozygosity**（想法）— 适合植物的污染检查：测序空白对照、竞争性比对和物种组成，以及杂合度过高。母本组织与胚的混合也会使等位比例偏离 0.5，可能被误当成污染。 输入：BAMs, blanks。输出：QC decision。版本：n/a（methods practice; no single software DOI）。  
  注：Treat a maternal-plus-embryo tissue mixture and present-day DNA contamination as competing explanations when allele ratios or heterozygosity look unusual. Allele ratios alone cannot separate the two. See the pre-registered two-genotype mixture test in section 13.
- **PMD-filter drift check (idea)**（想法）— 分别用 PMDtools 过滤后和全部读段做 PCA 投射和 f4。位置明显漂移，提示可能有现代葡萄 DNA 污染。这一检查可用于植物；hapCon 不能。 输入：BAM。输出：two projection results to compare。版本：n/a（uses PMDtools already in this catalogue）。 [doi:10.1073/pnas.1318934111](https://doi.org/10.1073/pnas.1318934111) · [link](https://github.com/pontussk/PMDtools)

<a id="section-11"></a>
## 11. 低覆盖度基因分型与补全

<!-- PROSE:SECTION:A11 -->
先用基因型似然或伪单倍型调用。伪单倍型调用是在每个位点随机抽取一条读段，虽对等位基因本身无偏，但会丢失个体内部的杂合信息，因此不能直接用于估算杂合度。在低覆盖度下，杂合位点按多数原则判定会产生偏倚，应改用随机抽取或基因型似然法；这一点在高度杂合的葡萄中比在人类数据中影响更为显著。仅在利用降采样现代样本完成预注册准确性测试后，方可使用 GLIMPSE2 进行基因型填充。单链文库的 pileupCaller 调用应添加 `--singleStrandMode` 参数。
<!-- /PROSE:SECTION:A11 -->

**分组：**
- *Imputation after a modern-downsample test (alternatives)*：GLIMPSE2。
- *Low-coverage calling (alternatives)*：ANGSD haploid calls and genotype likelihoods, ATLAS, sequenceTools pileupCaller。

- **GLIMPSE2**（工具）— 只有在把现代样本降到相同深度并测过准确性之后，才对古代葡萄基因组做补全（AM17，项目 20）。 输入：low-coverage BAM or GLs, modern haplotype panel。输出：imputed VCF。版本：2.0.0（GitHub odelaneau/GLIMPSE tag v2.0.0 (latest stable), 2026-11-14 CST; v2.0.1 is a GitHub pre-release and is not used as the catalogue version）。 [doi:10.1038/s41588-023-01438-3](https://doi.org/10.1038/s41588-023-01438-3) · [link](https://github.com/odelaneau/GLIMPSE)  
  注：For aDNA, test accuracy on modern grapes downsampled to ancient depths first (AM17, project 20). GitHub v2.0.1 is marked pre-release (checked 2026-11-14 CST); Bioconda glimpse-bio may still list 2.0.1. This catalogue pins the latest stable tag, 2.0.0, consistent with not using RC or beta tags as the catalogue version.
- **ANGSD haploid calls and genotype likelihoods**（工具）— 更推荐的似然路径：在极低覆盖度下不要强行做二倍体基因型。结构分析可用随机单倍型抽取或基因型似然。 输入：BAM, sites list。输出：haploid calls, genotype likelihoods。版本：0.940（see vitis-popgen section 2）。 [doi:10.1186/s12859-014-0356-4](https://doi.org/10.1186/s12859-014-0356-4) · [link](https://github.com/ANGSD/angsd)  
  注：For no-UDG data, consider transversion-only analyses. Grapevine heterozygosity makes naive majority-call genotypes noisy.
- **ATLAS**（工具）— 考虑损伤的古DNA检测器。见到了 Bioconda 的 2.0.4；钉版本前请确认 bitbucket 来源。 输入：BAM。输出：likelihoods or VCF。版本：2.0.4 (Bioconda atlas)（Bioconda atlas 2.0.4; expected Wegmann-lab source not resolved on GitHub in this check）。 [link](https://bitbucket.org/wegmannlab/atlas)  
  注：URL and exact upstream tag [待确认].
- **sequenceTools pileupCaller**（工具）— 从 pileup 做伪单倍型调用，常用来把古DNA放到现代 SNP 面板上。 输入：BAM, SNP list。输出：EIGENSTRAT or haploid VCF。版本：1.6.0.0（GitHub stschiff/sequenceTools + Bioconda, 2026-11-14 CST）。 [link](https://github.com/stschiff/sequenceTools)  
  注：For single-stranded libraries use `--singleStrandMode` (available since v1.4.0). For no-UDG data, drop transition sites or otherwise account for damage. Keep the SNP set matched to the modern panel. Version v1.6.0.0 matches the GitHub release (2026-01-28).

<a id="section-12"></a>
## 12. 测年

<!-- PROSE:SECTION:A12 -->
优先对同一粒种子或配对种子开展放射性碳测年，并结合标本馆的采集年份信息。分子末端定年应使用颠换位点或经 UDG 处理的数据。末端定年反映的是种子的死亡年代，而克隆基因型的起源可能更为古老。若古葡萄籽与现存栽培品种属于同一克隆，分子末端定年基本不提供有效时间信息。
<!-- /PROSE:SECTION:A12 -->

**分组：**
- *Molecular tip dating (alternatives, use transversions)*：BEAST 2, LSD2, TreeTime, Separate seed death date from clone origin (idea)。
- *Radiocarbon and calibration (complementary)*：AMS radiocarbon on the same seed or a paired seed, Bchron, rcarbon。

- **BEAST 2**（工具）— 古代葡萄序列的末端定年。应限制在颠换或 UDG 处理过的数据，并用末端随机化做检验。 输入：alignment, dates。输出：dated trees。版本：2.7.8（see vitis-popgen section 3）。 [link](https://www.beast2.org/)  
  注：Herbarium sheets with a collection year are safer tips than poorly dated seeds. Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **LSD2**（工具）— 对带日期末端的树做最小二乘定年。 输入：tree, dates。输出：dated tree。版本：2.4.1（GitHub tothuhien/lsd2 + Bioconda, 2026-11-14 CST）。 [link](https://github.com/tothuhien/lsd2)  
  注：Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **TreeTime**（工具）— 快速时间树放置，主要作为合理性检查，而不是葡萄驯化时钟。 输入：tree, dates。输出：time tree。版本：0.12.1（GitHub neherlab/treetime + Bioconda, 2026-11-14 CST）。 [link](https://github.com/neherlab/treetime)  
  注：Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **Separate seed death date from clone origin (idea)**（想法）— 碳十四或末端定年给出的是种子的死亡年代。克隆基因型可能更早就已存在。如果古籽与现存品种是同一克隆，分子分支长度近乎为零，末端定年没有信息量。 输入：AMS dates and, if used, molecular alignments。输出：model settings that keep the two times distinct。版本：n/a（methods and genetics reviews, 2026-11-14 CST）。
- **AMS radiocarbon on the same seed or a paired seed**（方案）— 材料允许时对同一个体测年，否则对同一背景中密切关联的种子测年。 输入：tissue or associated seed。输出：radiocarbon date。版本：n/a（used in Cohen et al. 2023 and Inanli et al. 2026 among others）。 [doi:10.1073/pnas.2213563120](https://doi.org/10.1073/pnas.2213563120) · [link](https://doi.org/10.1073/pnas.2213563120)  
  注：Cohen et al. 2023 is one grape example that combined aDNA and radiocarbon. Calibration curve choice (IntCal) belongs in the lab report.
- **Bchron**（工具）— 在 R 中做贝叶斯碳十四校正和年代学。 输入：radiocarbon determinations。输出：calibrated dates。版本：4.7.8（CRAN Bchron, 2026-11-14 CST）。 [link](https://cran.r-project.org/package=Bchron)
- **rcarbon**（工具）— 碳十四校正、SPD 和年代汇总工具。 输入：dates。输出：calibrated distributions。版本：1.5.2（CRAN rcarbon, 2026-11-14 CST）。 [link](https://cran.r-project.org/package=rcarbon)  
  注：OxCal is widely used but is a vendor application; version was not checked in this build [待确认].

<a id="section-13"></a>
## 13. 与现代样本的下游群体遗传分析

<!-- PROSE:SECTION:A13 -->
将样本投射至去克隆后的现代样本 PCA 空间，计算 f 统计量，并检验其与现用品种的身份。“同一克隆”与“一级亲缘”的结论必须分开表述，因为二者均依赖于尚未直接验证的组织来源假设。与 vitis-popgen 的内容重叠在预期之内。低覆盖度亲缘分析请选用经过校准的工具，切勿直接套用 KING 的硬判定阈值。同一考古单元出土的种子可能互为同胞，要先检查亲缘。本节预注册的混合检验用于区分单一基因型与混合状态；若存在胚乳，则需采用两参数模型；仅凭等位基因比例既无法区分组织混合与现代污染，也无法判定母本组分。
<!-- /PROSE:SECTION:A13 -->

**分组：**
- *Clone matching through time (complementary)*：Identity to living cultivars, READv2, KIN (KINgaroo), BREADR, Pre-registered allele-ratio test for seed-tissue mixture (idea)。
- *Projecting onto moderns (in order)*：ADMIXTOOLS 2 f-statistics and qpAdm, hapROH on ancient cultivars, smartpca lsqproject, Process modern samples on the same footing (idea)。
- *ROH and heterozygosity at low coverage (alternatives)*：ROHan。
- *Relatedness within an archaeological unit (complementary)*：Sibling check among seeds from the same unit (idea)。

- **Identity to living cultivars**（想法）— 检验一粒古籽与现存品种是同一克隆、一级亲缘，还是仅仅来自同一更大的群体。这些结论依赖于未经直接验证的组织来源假设，也依赖于污染控制。 输入：ancient and modern genotypes。输出：kinship or IBS, with contamination checks。版本：n/a（results reported in Ramos-Madrigal 2019, Noraz 2026, Pérez-Jordà 2026）。 [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://doi.org/10.1038/s41477-019-0437-5)  
  注：Same-clone language is only straightforward if the DNA mainly represents maternal seed-coat tissue. If it mainly represents the embryo, a parent-offspring relationship is the expected match to the mother cultivar. Distinguish same-clone from first-degree results in the write-up. Use low-coverage kinship tools (READv2, KIN, BREADR; calibrate on modern pairs downsampled to the same depth), not a generic 'kinship or IBS' cutoff and not KING hard-call thresholds. Molecular tip-dating is uninformative if the pip is the same clone as a living cultivar.
- **READv2**（工具）— 用伪单倍型低覆盖数据的两两错配率估计亲缘（可到三级）。按人类数据开发，用于葡萄时要用降到相同深度的现代克隆对和亲缘对校准。Noraz 等 2026（doi:10.1038/s41467-026-70166-z）曾用 VIVC 为葡萄克隆做过校准，已在 2026-11-14 的文献复审中对照该文确认。 输入：pseudo-haploid PLINK or EIGENSTRAT。输出：relatedness class。版本：2.1.1（GitHub GuntherLab/READv2 release 2.1.1, checked 2026-11-14 CST）。 [doi:10.1186/s13059-024-03350-3](https://doi.org/10.1186/s13059-024-03350-3) · [link](https://github.com/GuntherLab/READv2)  
  注：This is the current READ lineage; the original READ paper (10.1371/journal.pone.0195491) is not a second tool entry.
- **KIN (KINgaroo)**（工具）— 用隐马尔可夫模型从低覆盖数据识别 IBD 片段（人类测试中可到约 0.05 倍），可选污染校正和 ROH 模型。用于葡萄需要校准。 输入：BAM via KINgaroo。输出：relatedness class and IBD segments。版本：v3.1.4（GitHub DivyaratanPopli/Kinship_Inference release v3.1.4, checked 2026-11-14 CST）。 [doi:10.1186/s13059-023-02847-7](https://doi.org/10.1186/s13059-023-02847-7) · [link](https://github.com/DivyaratanPopli/Kinship_Inference)
- **BREADR**（工具）— 针对极低覆盖伪单倍型数据，给出 identical/twins、一级、二级或无关的后验概率。校准后，identical 类可用于古籽与现存品种的克隆匹配。 输入：EIGENSTRAT。输出：relatedness-class posteriors。版本：1.1.0（CRAN BREADR 1.1.0, checked 2026-11-14 CST）。 [doi:10.32614/CRAN.package.BREADR](https://doi.org/10.32614/CRAN.package.BREADR) · [link](https://cran.r-project.org/package=BREADR)
- **Pre-registered allele-ratio test for seed-tissue mixture (idea)**（想法）— 若有高深度古籽，预先登记一项混合检验：在至少一个推断基因型上为杂合的位点进行分析。种皮加胚的混合是两个二倍体基因型，母本（种皮）DNA 占比为 m；次要等位的预期比例随 m 连续变化：母本 AA、胚 AB 的位点，B 的比例约为 (1−m)/2；母本 AB、胚 AA 的位点，约为 m/2；二者都杂合的位点仍接近 0.5。单一的 0.5 峰与一个二倍体基因型相符；偏离 0.5 的额外分量与混合相符。1/3（或 2/3）峰只是纯胚乳的特例，例如母本 AA 加上父本贡献的 B（胚乳 AAB）。若同时有胚乳 DNA，这粒籽在单倍型上仍是母本与父本来源单倍型的混合（卵细胞和极核来自同一大孢子，同一花粉粒的两个精子基因型相同），但单个 m 不再等于种皮占比，需要两参数的三单倍型模型。单看等位比例既不能判断哪个成分是母本，也不能把组织混合与现代污染分开，因为二者都是基因型混合。三等位位点只作辅助指标。要把组织混合与现代污染分开，主要证据是：（i）按损伤分层，看只用带末端 C→T 的读段时次要基因型是否仍在；（ii）片段长度分布。亲子检验只是辅助：它可以排除无关的现代污染，但不能排除来自亲缘品种的污染；亲子约束本身必须包括自交（父本就是母本）。预注册阈值仍为 [待确认]，必须在分析任何古样本之前锁定；本目录不编造这些数字。 输入：high-depth BAM or VCF。输出：mixture-model fit, allele-ratio histogram, auxiliary triallelic count。版本：n/a（catalogue revision, 2026-11-14 CST）。  
  注：设计说明，所有数值门槛仍为 [待确认]，此处不公布数字：主分析只用颠换位点；用似然比检验加参数自助法，比较单一基因型模型、无约束混合模型，以及加了亲子约束的混合模型（亲子约束必须包括自交，即父本就是母本；贝叶斯版本若使用，只作敏感性分析）。第二层判别组织混合还是现代污染，应主要依据损伤分层或 PMD 读段以及片段长度分布。亲子似然比只能排除无关的污染源；来自亲缘品种的现代污染仍可能通过这项检验。阴性对照（现代样本降采样并加上损伤）和阳性对照（在电脑上混合亲子对、加入自交情景、胚乳情景，以及无关污染和亲缘品种污染）应在看到古数据之前完成，并锁定门槛。这里复查过的已发表古葡萄籽研究没有报告这项检验。Li 和 Berger 2012（10.1111/j.1469-8137.2012.04182.x）是一篇关于胚乳发育的综述。胚乳两份母本、一份父本基因组的比例，此处按被子植物的常见情况陈述 [待确认]。Le 等 2026（10.1111/1755-0998.70210）只把种子组织倍性作为稻和大麦的背景提到。
- **ADMIXTOOLS 2 f-statistics and qpAdm**（工具）— 在预先登记分组后，用古代和现代群体做 f3、f4 和 qpAdm。 输入：genotype blocks。输出：f-statistics, admixture models。版本：2.0.1（see vitis-popgen section 6）。 [doi:10.7554/elife.85492](https://doi.org/10.7554/elife.85492) · [link](https://github.com/uqrmaie1/admixtools)  
  注：Overlap with vitis-popgen is intentional.
- **hapROH on ancient cultivars**（工具）— 借助单倍型参考面板，从低覆盖度数据检测 ROH。按人类数据（1240k / 千人基因组面板）开发和测试。不能用来推断无性系历史：克隆繁殖不产生 ROH。 输入：haploid calls, modern panel。输出：ROH。版本：0.70（see vitis-popgen section 8）。 [doi:10.1038/s41467-021-25289-w](https://doi.org/10.1038/s41467-021-25289-w) · [link](https://github.com/hringbauer/hapROH)  
  注：Human-specific as distributed. Use on Vitis only after building a Vitis phased haplotype panel and validating on modern grapes downsampled to the target depth; unvalidated results must not be reported. ROH reflects inbreeding at the sexual origin of the sampled genotype, not centuries of clonal propagation. Prefer species-general ROHan, or bcftools roh when depth is sufficient. Newest is 0.70 on GitHub/PyPI; Bioconda lagged at 0.64.
- **smartpca lsqproject**（工具）— 把古代样本投射到去克隆后的现代葡萄 PCA 上，而不让它们决定坐标轴。 输入：modern EIGENSTRAT, ancient genotypes。输出：projected PCs。版本：see vitis-popgen section 2（EIGENSOFT, version caveat unchanged）。 [link](https://github.com/DReichLab/EIG)  
  注：Missingness and damage can still shift projections; report coverage and transition/transversion choices.
- **Process modern samples on the same footing (idea)**（想法）— 做 PCA 投射或 f 统计之前，现代样本要用同一 SNP 集做伪单倍型化，做同样的颠换过滤，必要时降到古样本深度，避免把技术差异当成群体差异。 输入：modern BAM or VCF。输出：matched genotype matrix。版本：n/a（methods review, 2026-11-14 CST）。
- **ROHan**（工具）— 从单个 BAM 联合估计杂合度和 ROH，可做损伤校正，不依赖人类单倍型面板。可作为 hapROH 的物种通用替代。原文摘要给出的可用覆盖度为：现代样本低至 5−6 倍，有中等损伤的古代样本低至 7−8 倍。 输入：BAM。输出：heterozygosity and ROH tracts。版本：v1.0.7（GitHub grenaud/ROHan release v1.0.7, checked 2026-11-14 CST）。 [doi:10.1534/genetics.119.302057](https://doi.org/10.1534/genetics.119.302057) · [link](https://github.com/grenaud/ROHan)  
  注：ROH still reflects inbreeding at sexual origin, not clonal history.
- **Sibling check among seeds from the same unit (idea)**（想法）— 同一层位、甚至同一串果里的种子可能是全同胞或半同胞。在估计等位频率、做 PCA 或 f 统计之前，要先检查亲缘，再修剪或建模，逻辑与现代样本相同。 输入：low-coverage genotypes from co-located pips。输出：relatedness table and a pruned or modelled set。版本：n/a（genetics review, 2026-11-14 CST）。

<a id="section-14"></a>
## 14. 工作流与流程

<!-- PROSE:SECTION:A14 -->
nf-core/eager 2.5.3 为默认的社区流程（AM17），其适用的 Nextflow 版本上限为 22.10.6。本仓库已于 2026-10-21 已有捕获相关脚本。
<!-- /PROSE:SECTION:A14 -->

**分组：**
- *Community workflows (alternatives)*：EAGER (legacy Java pipeline), PALEOMIX, nf-core/eager。
- *This repository (complementary)*：Existing capture scripts and notes。

- **EAGER (legacy Java pipeline)**（流程）— 最初的 EAGER 流程。只用来理解旧论文；新分析请用 nf-core/eager。 输入：FASTQ。输出：BAM, QC。版本：see Peltzer 2016; superseded by nf-core/eager for new work（Peltzer et al. 2016 DOI verified）。 [doi:10.1186/s13059-016-0918-z](https://doi.org/10.1186/s13059-016-0918-z) · [link](https://doi.org/10.1186/s13059-016-0918-z)
- **PALEOMIX**（流程）— 古DNA比对、过滤和下游系统发育步骤的备选流程。 输入：FASTQ, reference。输出：BAM, phylogenetic inputs。版本：1.4.1（GitHub MikkelSchubert/paleomix, 2026-11-14 CST）。 [doi:10.1038/nprot.2014.063](https://doi.org/10.1038/nprot.2014.063) · [link](https://github.com/MikkelSchubert/paleomix)  
  注：Schubert et al. 2014 Nature Protocols DOI verified.
- **nf-core/eager**（流程）— AM17 中的默认端到端古DNA流程：AdapterRemoval、bwa aln、DamageProfiler 或 mapDamage、DeDup 或 MarkDuplicates、Qualimap、preseq，可选 PMDtools、Kraken2/MALT。 输入：FASTQ, reference。输出：BAM, damage, QC MultiQC。版本：2.5.3（GitHub nf-core/eager 2.5.3 (2025-03-18); 3.0 Augsburg is not released (open milestone, 2026-11-14 CST)）。 [doi:10.7717/peerj.10947](https://doi.org/10.7717/peerj.10947) · [link](https://nf-co.re/eager)  
  注：This is DSL1 and requires Nextflow >=20.07.1 and <=22.10.6. Version 3.0 is not released. Human contamination modules (ANGSD X-chromosome) must be turned off or ignored for grape.
- **Existing capture scripts and notes**（流程）— 本仓库已有：AdapterRemoval、bwa aln、samtools q30、Picard MarkDuplicates、Qualimap、mapDamage，以及比对统计汇总。 输入：paired FASTQ, VS1.final.fa (path is a placeholder in the notes)。输出：per-sample BAM, damage, stats.all.tsv。版本：GitHub main fe75e89e, 2026-10-21 22:19 CST（Xuzhen-Li/grapevine-adna main, read-only audit 2026-11-14）。 [link](https://github.com/Xuzhen-Li/grapevine-adna/tree/main/scripts)  
  注：文件：scripts/adna_capture_pipeline_generator.sh、dsdna_preprocess.sh、collect_mapping_stats.sh、run_mapdamage.sh；notes/cap_test.md、check_pcrbias.md、mergeBAM.md。这些是仓库里已有的材料，属于捕获测试的生物信息流程。

<a id="section-15"></a>
## 15. 植物与葡萄的特殊问题

<!-- PROSE:SECTION:A15 -->
抑制剂和多酚、缺乏哺乳动物式的 X 染色体污染估算指标、性别决定区仅为 2 号染色体上的一小段而非异形性染色体、PN40024 参考基因组偏差，以及跨越数个世纪的无性系身份判定。质体序列是母系的，但在葡萄属内分辨率较低；NUPT 和 NUMT 插入片段会看起来像异质性。
<!-- /PROSE:SECTION:A15 -->

**分组：**
- *Reviews and plant-specific issues (complementary)*：Grape-specific analytical issues, Latorre et al. 2020 plant aDNA protocols, Ramos-Madrigal et al. 2026 plant palaeogenomics review, Kistler et al. 2020 plant aDNA review, Gutaker and Burbano 2017 plant aDNA, Meiri 2024 fruit paleogenomics。

- **Grape-specific analytical issues**（想法）— 植物和葡萄的注意点：抑制剂和多酚；没有哺乳动物那种用 X 染色体剂量估计污染的办法；性别决定区是 2 号染色体上的一小段，不是异形性染色体；栽培品种大多是两性花；质体数据是母系的，但在葡萄属内分辨率低，还可能被核基因组中的质体/线粒体插入（NUPT、NUMT）干扰；PN40024 参考偏差；跨世纪的无性系身份。 输入：n/a。输出：n/a。版本：n/a（synthesis of DS14, project 20, and this audit）。  
  注：Human X-chromosome contamination modules, including hapCon, do not transfer. See also grapevine-plastid for plastid assembly, and vitis-open-directions item 22 for sex-determining-region genotypes.
- **Latorre et al. 2020 plant aDNA protocols**（文献）— 植物古DNA提取、建库和生物信息分析的端到端方案。 输入：n/a。输出：n/a。版本：n/a（Crossref title match）。 [doi:10.1002/cppb.20121](https://doi.org/10.1002/cppb.20121) · [link](https://doi.org/10.1002/cppb.20121)
- **Ramos-Madrigal et al. 2026 plant palaeogenomics review**（文献）— 植物古基因组学短综述：转向全基因组数据、驯化观念的变化、植物与微生物共演化、沉积物 DNA，以及失去的遗传多样性在作物改良中的用途。 输入：n/a。输出：n/a。版本：n/a（Crossref title match; journal year 2026, DOI has 2025 suffix）。 [doi:10.1016/j.pbi.2025.102856](https://doi.org/10.1016/j.pbi.2025.102856) · [link](https://doi.org/10.1016/j.pbi.2025.102856)  
  注：Wording follows the abstract (EuropePMC PMID 41610813). The abstract does not mention polyphenols, PCR inhibitors, single-stranded libraries, authentication, or grape tannins. Those topics should be cited from the Gansauge ss-library series and from Bolognesi 2025 / Wales 2014, not from this review, unless someone has read the full text [待确认].
- **Kistler et al. 2020 plant aDNA review**（文献）— 关于考古、标本馆和沉积物中植物古DNA的综述。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1146/annurev-arplant-081519-035837](https://doi.org/10.1146/annurev-arplant-081519-035837) · [link](https://doi.org/10.1146/annurev-arplant-081519-035837)
- **Gutaker and Burbano 2017 plant aDNA**（文献）— 面向进化基因组学的植物古DNA短综述。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1016/j.pbi.2017.01.002](https://doi.org/10.1016/j.pbi.2017.01.002) · [link](https://doi.org/10.1016/j.pbi.2017.01.002)
- **Meiri 2024 fruit paleogenomics**（文献）— 包括葡萄在内的果树作物古基因组综述。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1016/j.tig.2024.02.003](https://doi.org/10.1016/j.tig.2024.02.003) · [link](https://doi.org/10.1016/j.tig.2024.02.003)

<a id="section-16"></a>
## 16. 关键研究、公开数据与模拟

<!-- PROSE:SECTION:A16 -->
DS14 中已收录的公开发表葡萄古DNA数据集，以及用于流程测试的模拟数据生成器。本仓库不包含任何未发表的基因型数据。
<!-- /PROSE:SECTION:A16 -->

**分组：**
- *Public grape aDNA datasets (complementary)*：DS14 archaeological grape seed sequencing, Cohen 2023 ancient pip reads, Inanli 2026 reads。
- *Simulation of aDNA reads (complementary)*：gargammel, ngsngs。
- *Related ancient-plant studies (complementary)*：Mascher et al. 2016 ancient barley, Kistler et al. 2017 DNA decay model。

- **DS14 archaeological grape seed sequencing**（资源）— PRJNA489970（法国捕获）、PRJEB89110（切塔穆拉）、PRJEB94459（法国 4000 年）、PRJNA999173（佩尔托萨洞，关联论文 [待确认]）。 输入：ENA。输出：FASTQ。版本：accessions listed 2026-11-14 in vitis-open-directions（DS14 README, sizes from ENA on 2026-11-14）。 [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://www.ebi.ac.uk/ena/browser/view/PRJNA489970)  
  注：No unpublished genotypes. figshare 10.6084/m9.figshare.7610987 licence [待确认].
- **Cohen 2023 ancient pip reads**（资源）— ENA PRJNA887039，标题为 Ancient Negev grape DNA（20 个 run）。文献核对记录的现代面板：PRJNA887737、PRJNA647155。 输入：n/a。输出：n/a。版本：n/a（ENA accession checked in the literature review, 2026-11-14 CST）。 [link](https://www.ebi.ac.uk/ena/browser/view/PRJNA887039)  
  注：This is an accession, not a DOI.
- **Inanli 2026 reads**（资源）— ENA PRJEB89110，标题与 Inanli 等 2026 论文相符（首次公开 2026-05-31）。 输入：n/a。输出：n/a。版本：n/a（ENA accession checked in the literature review, 2026-11-14 CST）。 [link](https://www.ebi.ac.uk/ena/browser/view/PRJEB89110)  
  注：This is an accession, not a DOI.
- **gargammel**（工具）— 模拟带损伤、片段长度和污染的古DNA读段，用于测试流程。 输入：reference, parameters。输出：FASTQ。版本：1.2.0（GitHub grenaud/gargammel + Bioconda, 2026-11-14 CST）。 [link](https://github.com/grenaud/gargammel)  
  注：Use before trusting project-20 imputation thresholds.
- **ngsngs**（工具）— 灵活的 NGS 读段模拟器，也可加入类似古DNA的特征。 输入：reference, profile。输出：FASTQ。版本：0.9.2（GitHub/Bioconda ngsngs, 2026-11-14 CST）。 [link](https://github.com/rbaumannhansen/ngsngs)  
  注：Confirm aDNA parameters against the manual before using numbers in a preregistration.
- **Mascher et al. 2016 ancient barley**（文献）— 古代植物籽粒全基因组测序的例子。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1038/ng.3611](https://doi.org/10.1038/ng.3611) · [link](https://doi.org/10.1038/ng.3611)
- **Kistler et al. 2017 DNA decay model**（文献）— 基于 185 个古基因组数据集的 DNA 降解模型，材料以哺乳动物骨骼为主，植物种子可能不同。 输入：n/a。输出：n/a。版本：n/a（Crossref-verified in the literature review, 2026-11-14 CST）。 [doi:10.1093/nar/gkx361](https://doi.org/10.1093/nar/gkx361) · [link](https://doi.org/10.1093/nar/gkx361)

<a id="section-17"></a>
## 17. 同时收入 vitis-popgen 的工具

<!-- PROSE:SECTION:A17 -->
这些工具有意同时收录于两个目录中，其细节与版本完全一致；本列表仅作交叉对照，并非另一套独立的变异检测流程。与 vitis-popgen 共享的低覆盖度亲缘及 ROH 分析工具（READv2、KIN、BREADR、ROHan）已列于第 13 节，此处不再赘述。
<!-- /PROSE:SECTION:A17 -->

**分组：**
- *BAM processing (complementary)*：samtools。
- *Phasing and imputation of modern data (in order)*：GLIMPSE2。
- *Read QC (complementary)*：fastp。
- *Sample identity, before structure (complementary)*：KING。
- *BAM hygiene / post-mapping (complementary)*：Picard。
- *VCF QC and manipulation (complementary)*：bcftools。
- *Global ancestry (alternatives)*：ADMIXTURE。
- *Low-coverage genotype-likelihood methods (alternatives)*：ANGSD, PCAngsd。
- *PCA (alternatives)*：smartpca (EIGENSOFT)。
- *Bayesian or dated trees (alternatives)*：BEAST 2。
- *tsinfer then tsdate (in order)*：tsinfer。
- *SMC-style histories (alternatives)*：SMC++。
- *f-statistics and graphs (alternatives)*：ADMIXTOOLS 2, Dsuite。
- *ROH callers (alternatives)*：bcftools roh。
- *ROH callers, low coverage (alternatives)*：hapROH。
- *Kinship, IBD and clonality (complementary)*：ngsRelate。

- **samtools**（工具）— 排序、建索引、标记重复、过滤并汇报比对统计。 输入：SAM/BAM/CRAM。输出：BAM/CRAM, stats。版本：1.25（GitHub samtools/samtools + Bioconda, 2026-11-14 CST）。 [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008) · [link](https://github.com/samtools/samtools)  
  注：Same 1.25 line as bcftools and htslib. samtools is not a mapper; it belongs with BAM processing, not under Mapping.
- **GLIMPSE2**（工具）— 用单倍型参考面板补全低覆盖度基因组。 输入：low-coverage BAM or genotype likelihoods, reference panel。输出：imputed VCF。版本：2.0.0（GitHub odelaneau/GLIMPSE tag v2.0.0 (latest stable), 2026-11-14 CST; v2.0.1 is a GitHub pre-release and is not used as the catalogue version）。 [doi:10.1038/s41588-023-01438-3](https://doi.org/10.1038/s41588-023-01438-3) · [link](https://github.com/odelaneau/GLIMPSE)  
  注：For aDNA, test accuracy on modern grapes downsampled to ancient depths first (AM17, project 20). GitHub v2.0.1 is marked pre-release (checked 2026-11-14 CST); Bioconda glimpse-bio may still list 2.0.1. This catalogue pins the latest stable tag, 2.0.0, consistent with not using RC or beta tags as the catalogue version.
- **fastp**（工具）— 修剪接头和低质量碱基，并写出质控报告。 输入：FASTQ。输出：trimmed FASTQ, HTML/JSON QC。版本：1.4.0（GitHub OpenGene/fastp + Bioconda, checked 2026-11-14 CST）。 [link](https://github.com/OpenGene/fastp)  
  注：GitHub release 2026-10-07. Also in vitis-open-directions AM02.
- **KING**（工具）— 用于区分克隆/重复与一级亲缘的稳健亲缘估计。克隆和重复（亲缘系数高于 0.354）每组只留一个样本；一级亲缘（0.177-0.354）只登记，不当作同一基因型删掉。 不是低覆盖古籽的默认方法。 输入：hard-called diploid genotypes (BED)。输出：kinship tables。版本：2.3.2（Bioconda king, 2026-11-14 CST）。 [doi:10.1093/bioinformatics/btq559](https://doi.org/10.1093/bioinformatics/btq559) · [link](https://www.kingrelatedness.com/)  
  注：Thresholds follow the KING manual (https://www.kingrelatedness.com/manual.shtml): kinship above 0.354 is the duplicate/MZ class; 0.177-0.354 is first-degree. Paper: Manichaikul et al. 2010, 10.1093/bioinformatics/btq559. AM26 used 0.177 as the first-degree lower cutoff. Input should be hard-called diploid genotypes (BED). For low-coverage or ancient samples use ngsRelate, READv2, KIN or BREADR instead. Handling of first-degree relatives is analysis-specific; see docs/WORKFLOW.md.
- **Picard**（工具）— MarkDuplicates、读组、CleanSam 等 BAM 整理。 输入：BAM/SAM。输出：BAM, metrics。版本：3.5.0（GitHub broadinstitute/picard + Bioconda, 2026-11-14 CST）。 [link](https://github.com/broadinstitute/picard)  
  注：Picard works on BAM (MarkDuplicates, read groups, CleanSam), not on VCF. GitHub release 2026-07-31 CST-relative: 2026-08-01 02:56 CST. For collapsed aDNA reads, DeDup is the default duplicate marker; see section 8.
- **bcftools**（工具）— 过滤、规范化、注释、统计，以及 ROH 检测（见第 8 节）。 输入：VCF/BCF or BAM。输出：VCF/BCF, tables。版本：1.25（GitHub samtools/bcftools + Bioconda, 2026-11-14 CST）。 [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008) · [link](https://github.com/samtools/bcftools)
- **ADMIXTURE**（工具）— 最大似然祖源比例，AM13 的默认工具。 输入：BED, LD-pruned SNPs。输出：Q and P matrices。版本：1.3.0（Bioconda admixture, 2026-11-14 CST）。 [doi:10.1101/gr.094052.109](https://doi.org/10.1101/gr.094052.109) · [link](https://dalexander.github.io/admixture/)  
  注：Clone-prune first (one sample per clone or duplicate group). First-degree relatives should not be dropped as if they were the same genotype; for ADMIXTURE use an unrelated subset or report a sensitivity analysis (see docs/WORKFLOW.md). Choose K with cross-validation and inspect fit with evalAdmix.
- **ANGSD**（工具）— 从 BAM 计算基因型似然、等位基因频率、SFS、关联和单倍型调用。 输入：BAM, reference。输出：genotype likelihoods, SFS, MAF, haploid calls。版本：0.940（GitHub ANGSD/angsd + Bioconda, 2026-11-14 CST）。 [doi:10.1186/s12859-014-0356-4](https://doi.org/10.1186/s12859-014-0356-4) · [link](https://github.com/ANGSD/angsd)  
  注：Central for aDNA and low-coverage modern data. Human X-chromosome contamination utilities do not transfer to grape.
- **PCAngsd**（工具）— 用基因型似然做 PCA 和类混合结构分析，适用于低覆盖度。 输入：ANGSD-style genotype likelihoods。输出：principal components, admixture。版本：1.37.0（GitHub Rosemeis/pcangsd 2026-10-23; Bioconda/PyPI 1.36.4）。 [doi:10.1534/genetics.118.301336](https://doi.org/10.1534/genetics.118.301336) · [link](https://github.com/Rosemeis/pcangsd)  
  注：Newest GitHub tag is 1.37.0; Bioconda lagged at 1.36.4.
- **smartpca (EIGENSOFT)**（工具）— 带收缩和 lsqproject 的 PCA，通常用来把古DNA投射到现代 PCA 上。 输入：EIGENSTRAT。输出：eigenvectors, projected PCs。版本：9.0.0 (Bioconda); GitHub tag v8.0.0 [待确认] (numbering)（Bioconda eigensoft 9.0.0; DReichLab/EIG GitHub tag v8.0.0）。 [doi:10.1371/journal.pgen.0020190](https://doi.org/10.1371/journal.pgen.0020190) · [link](https://github.com/DReichLab/EIG)  
  注：Pin the exact binary. Bioconda and GitHub numbers disagree.
- **BEAST 2**（工具）— 有时间校准时可做贝叶斯树和末端定年。 输入：alignment, priors。输出：trees, dates。版本：2.7.8（GitHub CompEvol/beast2 + Bioconda, 2026-11-14 CST）。 [link](https://www.beast2.org/)  
  注：For aDNA tip-dating use transversions or UDG-treated data. Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **tsinfer**（工具）— 从已定相的大样本推断树序列（ARG 的近似）。 输入：phased genotypes。输出：tree sequence。版本：0.5.1（conda-forge tsinfer, 2026-11-14 CST (also AM14)）。 [doi:10.1038/s41588-019-0483-y](https://doi.org/10.1038/s41588-019-0483-y) · [link](https://github.com/tskit-dev/tsinfer)  
  注：Pair with tsdate. Clone-prune and deal with close kinship first (AM14, project 10).
- **SMC++**（工具）— 从许多未定相基因组推断有效种群大小历史。 输入：VCF, population labels。输出：Ne trajectory。版本：1.15.2（GitHub popgenmethods/smcpp + Bioconda, 2026-11-14 CST）。 [doi:10.1038/ng.3748](https://doi.org/10.1038/ng.3748) · [link](https://github.com/popgenmethods/smcpp)  
  注：Reduce clones and duplicates to one sample per group. For recent Ne, also remove or model first-degree relatives (see docs/WORKFLOW.md).
- **ADMIXTOOLS 2**（工具）— 在 R 中计算 f2、f3、f4、qpAdm 和 qpGraph，并做区组刀切。 输入：genotype or f2 blocks。输出：f-statistics, admixture graphs。版本：2.0.1（GitHub uqrmaie1/admixtools v2.0.1, 2026-11-14 CST (also AM13)）。 [doi:10.7554/elife.85492](https://doi.org/10.7554/elife.85492) · [link](https://github.com/uqrmaie1/admixtools)  
  注：Default alternative in AM13. Maier et al. 2023 eLife DOI verified.
- **Dsuite**（工具）— 快速计算 D、f4 比值和 f-branch，并做区组刀切。 输入：VCF, tree or trio file。输出：D, f4, f-branch tables。版本：[待确认] (no tagged release)（GitHub millanek/Dsuite; no tag or Bioconda package in this check (same as AM13)）。 [doi:10.1111/1755-0998.13265](https://doi.org/10.1111/1755-0998.13265) · [link](https://github.com/millanek/Dsuite)  
  注：Version remains [待确认], as in AM13. The 2021 paper DOI was verified.
- **bcftools roh**（工具）— 用隐马尔可夫模型检测纯合片段。AM12 使用去克隆后按群体估计的等位基因频率，而不是默认频率文件。 输入：VCF, population AF file。输出：ROH tables。版本：1.25（same bcftools 1.25 as section 1; also AM12）。 [doi:10.1093/bioinformatics/btw044](https://doi.org/10.1093/bioinformatics/btw044) · [link](https://github.com/samtools/bcftools)  
  注：Default ROH tool in AM12. ROH method paper: Narasimhan et al. 2016, 10.1093/bioinformatics/btw044. The samtools/bcftools suite DOI 10.1093/gigascience/giab008 still applies to the package.
- **hapROH**（工具）— 借助单倍型参考面板，从低覆盖度数据检测 ROH。按人类数据（1240k / 千人基因组面板）开发和测试。不能用来推断无性系历史：克隆繁殖不产生 ROH。 输入：pseudo-haploid or low-coverage genotypes, reference panel。输出：ROH, inbreeding。版本：0.70（GitHub/PyPI hapROH 0.70; Bioconda 0.64）。 [doi:10.1038/s41467-021-25289-w](https://doi.org/10.1038/s41467-021-25289-w) · [link](https://github.com/hringbauer/hapROH)  
  注：Human-specific as distributed. Use on Vitis only after building a Vitis phased haplotype panel and validating on modern grapes downsampled to the target depth; unvalidated results must not be reported. ROH reflects inbreeding at the sexual origin of the sampled genotype, not centuries of clonal propagation. Prefer species-general ROHan, or bcftools roh when depth is sufficient. Newest is 0.70 on GitHub/PyPI; Bioconda lagged at 0.64.
- **ngsRelate**（工具）— 用基因型似然估计亲缘，适用于低覆盖度数据。 输入：ANGSD genotype likelihoods。输出：relatedness。版本：2.3.1（GitHub ANGSD/NgsRelate + Bioconda, 2026-11-14 CST）。 [doi:10.1093/gigascience/giz034](https://doi.org/10.1093/gigascience/giz034) · [link](https://github.com/ANGSD/NgsRelate)


## 2026-11-15 追加的教学章节

以上各行是仓库现有首页（提交 b6e4302e，2026-11-15 17:29 CST）。本节只追加，不替换首页。上面的每一行都保持原样。

本次更新在现有的 `README.md`、`README.zh.md` 和 `catalog/CATALOG.tsv` 末尾追加内容，并新增教学文件。不修改现有的 `scripts/02_map_adna.sh` 和 `scripts/03_dedup.sh`。README 和目录里已有的每一行都保持原样。

### 对现有首页行的勘误（只做指针；现有各行不改）

下面两条现有首页说法，在教学上由相应章节和目录勘误行取代。现有原文本身不改。

- 现有第 286 行（schmutzi：“为人类设计的线粒体污染估计。不是葡萄核基因组污染工具。”）— 见 [docs/03_contamination.md](docs/03_contamination.md) 和目录 E001 行。官方 schmutzi README 的 Nuclear 节写明，contDeam 可在所列前提下用于核数据，风险自负；核样本推荐 DICE。
- 现有第 264 行（pyDamage：“适合参考很多的情况（宏基因组或竞争性比对）”）— 见 [docs/02_authentication_damage.md](docs/02_authentication_damage.md) 和目录 E004 行。按 contig 估计损伤的说明面向宏基因组；不把它写成竞争性比对工具。

现有的 hapCon 备注（第 285 行）和现有目录 hapCon 行（CATALOG 第 40 行）写有 “Keep the entry as a warning, like schmutzi.” 这一比较由扩展后的 E001 勘误覆盖；这些现有行也不改。

### 校验清单

现有的 `SHA256SUMS`（本次更新不改）记录原始文件（`README.md`、`README.zh.md`、`ADDITIONS.tsv`、`catalog/CATALOG.tsv`、`docs/WORKFLOW.md` 和 `docs/WORKFLOW.zh.md`）的哈希。本次更新在 README 和目录末尾追加内容之后，那份较早清单里的 README 和 CATALOG 哈希将不再匹配。`SHA256SUMS.v2` 记录后来新增或追加的那些文件的哈希。`ADDITIONS.tsv` 是现有目录追加前的一份未改动的早期副本（与追加前的现有 CATALOG 哈希相同），本次更新不更新它。

### 新增或修订的教学文件

- `CHANGELOG.md` — 这些教学文件的公开修订摘要
- `SHA256SUMS.v2` — 后来新增或追加的那些文件的哈希（本次更新唯一的额外清单）
- `DOI_CHECKS.tsv`、`DOI_CHECKS.NOTES.md`
- `SOURCES_READ.tsv`
- `REMOVALS.md`、`REMOVALS.zh.md` — 仅建议淘汰清单，推荐方案 B，这里不删除任何文件
- `docs/01_published_grape_adna.md` 及 `.zh.md`
- `docs/02_authentication_damage.md` 及 `.zh.md`
- `docs/03_contamination.md` 及 `.zh.md`
- `docs/04_capture_shotgun_lowcov.md` 及 `.zh.md`
- `figures/F1_damage_patterns_by_library.svg`、`figures/F2_adna_decision_route.svg`
- `scripts/02_map_adna.v2.sh`、`scripts/03_dedup.v2.sh` — 新文件名下的帮助 / `--dry-run` 封装
- `scripts/figures/copy_adna_schematics.py` — 只复制上述两张 SVG，不生成图

现有的 `scripts/README.md` 不改。因此它的 “Tested?” 表仍只列出 `02_map_adna.sh` 和 `03_dedup.sh`，不会列出 `02_map_adna.v2.sh` 或 `03_dedup.v2.sh`。这两个 `.v2.sh` 封装只是帮助 / `--dry-run` 文档，并不替代现有脚本。它们列在本节和 [CHANGELOG.md](CHANGELOG.md) 中。

这些教学文件的修订记录见 [CHANGELOG.md](CHANGELOG.md)。
