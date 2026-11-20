# 2. Authentication and damage

Damage patterns are used to ask whether mapped reads look like ancient molecules. The tools below were read from their papers and/or GitHub READMEs in the sources opened for these chapters. None of them, by itself, declares a grape sample authentic.

## mapDamage and mapDamage2

Ginolhac et al. (2011, abstract; doi:10.1093/bioinformatics/btr347; print year 2011, online 9 June 2011), titled “mapDamage: testing for damage patterns in ancient DNA sequences,” is the original mapDamage paper (title-matched on Crossref and EuropePMC). Jónsson et al. (2013, abstract re-opened 2026-11-15 CST and full text previously recorded as PMC3694634; doi:10.1093/bioinformatics/btt193) describe mapDamage 2.0 as providing “fast approximate Bayesian estimates of ancient DNA damage parameters.” The same abstract states: “Our model enables rescaling base quality scores according to their probability of being damaged.” The GitHub README opened 2026-11-15 CST at https://github.com/ginolhac/mapDamage (1,995 bytes, sha256 b87e12ee9e574c25b4c696fa3cab31697a43fcbaf3ce4c6531a534bf55aad3e6, 2026-11-15 CST) mentions “plotting, modeling, and rescaling” only as a pointer to the dedicated documentation page; it does not itself describe a command mode that adjusts base qualities. Quality-score rescaling is therefore cited from the mapDamage 2.0 paper abstract, not from the README.

The thin wrapper already in this repository, `scripts/run_mapdamage.sh`, is a command template of the form `mapDamage -i <BAM> -r <REF> -d <OUT> --merge-reference-sequences` (the angle-bracket tokens are placeholders, not a verbatim invocation of `scripts/run_mapdamage.sh` line 6, which is `mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences`). That wrapper is proposed for keeping (see REMOVALS.md). It is not a substitute for reading the mapDamage 2.0 documentation before a production run.

## PMDtools, DamageProfiler and pyDamage

Skoglund et al. (2014, abstract; doi:10.1073/pnas.1318934111) introduced a method to separate endogenous ancient DNA from modern contamination using post-mortem damage, the basis of PMDtools (https://github.com/pontussk/PMDtools; README opened, 3,897 bytes). DamageProfiler (Neukamm et al. 2021, doi:10.1093/bioinformatics/btab190; README https://github.com/Integrative-Transcriptomics/DamageProfiler, 3,850 bytes, opened 2026-11-15 CST) is a damage-pattern calculator also documented in the nf-core/eager README. pyDamage (Borry et al. 2021, doi:10.7717/peerj.11845; README opened) estimates damage per contig and is described for metagenomic use; the opened README and paper do not support teaching it as a competitive-mapping tool, and it is not a grape-specific authenticator.

## Library type and UDG treatment

The opened Briggs and Rohland abstracts support the general statement that post-mortem damage is concentrated at molecule ends. They do not, in the text opened for these chapters, lay out the library-type mapping (double-stranded: 5-prime C-to-T and 3-prime G-to-A; single-stranded: C-to-T at both ends; UDG-half: residual damage in the terminal one or two bases), and that mapping is not a sentence in the existing WORKFLOW.md. Those more specific patterns remain **[待确认]** until a source that actually states them is opened. Rohland et al. (2015, doi:10.1098/rstb.2013.0624) should be cited for UDG-half from that paper’s own wording when the abstract is used; this chapter does not invent grape-specific trim lengths. Defaults such as trimming 2 nt from each end after UDG-half remain laboratory decisions unless a read source gives that number for the library type in use (**[待确认]** as a grape default).

## Full UDG and methylation: what Briggs 2010 actually says

Briggs et al. (2010, full text, PMC2847228; doi:10.1093/nar/gkp1163), “Removal of deaminated cytosines and detection of in vivo methylation in ancient DNA,” show that USER (UDG plus endonuclease VIII) removes uracils from ancient DNA, and that “Neandertal DNA retains in vivo patterns of CpG methylation.” That result is from Neandertal DNA and concerns CpG methylation. The sources opened for these chapters did not open a source that extends that residual C-to-T statement to plant CG, CHG or CHH contexts. Any such plant-context claim is **[待确认]** until a plant paper is read for it. The existing WORKFLOW sentence on plant CG/CHG/CHH is therefore not repeated here as an established fact.

## Herbarium damage kinetics

Weiß et al. (2016, abstract and full text, PMC4929915; doi:10.1098/rsos.160239), “Temporal patterns of damage and decay kinetics of DNA retrieved from plant herbarium specimens,” is a plant-herbarium damage study (title-matched). Porrelli et al. (2026, abstract; doi:10.1093/gigascience/giag026), “Patterns of aDNA damage through time and environments—lessons from herbarium specimens,” is a later herbarium-damage paper (abstract opened). Neither is a grape archaeological-pip dataset; both are relevant to how plant historical DNA degrades.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| mapDamage tests damage patterns in ancient DNA sequences | doi:10.1093/bioinformatics/btr347 | Title; abstract | EuropePMC abstract + Crossref title, 2026-11-15 CST |
| mapDamage 2.0: approximate Bayesian estimates of aDNA damage parameters; quality-score rescaling from the paper abstract, not the README | doi:10.1093/bioinformatics/btt193 | Abstract: “Our model enables rescaling base quality scores according to their probability of being damaged.” | Abstract re-opened 2026-11-15 CST (EuropePMC); full text previously recorded as PMC3694634. README (1,995 bytes, sha256 b87e12ee…) mentions “rescaling” only as a pointer to the docs page |
| PMDtools / Skoglund 2014: separate endogenous aDNA from modern contamination with post-mortem damage | doi:10.1073/pnas.1318934111 ; https://github.com/pontussk/PMDtools | Abstract; README | Abstract + README (3,897 bytes) |
| DamageProfiler is a damage-pattern calculator also documented in the nf-core/eager README | doi:10.1093/bioinformatics/btab190 ; https://github.com/Integrative-Transcriptomics/DamageProfiler | Paper title / README as opened 2026-11-15 CST (3,850 bytes) | Paper DOI + DamageProfiler README and nf-core/eager README |
| Briggs 2010: USER removes uracils; Neandertal DNA retains in vivo CpG methylation | doi:10.1093/nar/gkp1163 | Sentences quoted above | Full text (PMC2847228) |
| Residual C-to-T after full UDG in plant CG/CHG/CHH contexts | — | — | Not read in a plant source this addition; **[待确认]** |
| Weiß 2016: damage and decay kinetics in plant herbarium DNA | doi:10.1098/rsos.160239 | Title | Abstract + full text (PMC4929915) |
