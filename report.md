
---

## 1. Introduction

*Aedes aegypti* is the primary vector of dengue, Zika, chikungunya, and yellow fever viruses. Understanding the genetic relationships among mosquito populations across Kenya is important for tracking disease spread, identifying source populations, and informing vector control strategies. In this study, we reconstructed the phylogenetic relationships among Ae. aegypti populations sampled from multiple counties in Kenya using three genetic markers: cytochrome oxidase subunit I (COI), cytochrome b (CYTB), and internal transcribed spacer 2 (ITS2). We also compared two phylogenetic approaches, the coalescent based method ASTRAL and the supermatrix based method implemented in IQ TREE with a partitioned model scheme

## 2. Dataset Description

Sequences were retrieved from NCBI GenBank using Biopython and the Entrez API. A two stage search strategy was used, with Kenya specific queries conducted first and the search expanded to East African records or, when necessary, globally sourced sequences if fewer than 15 Kenyan sequences were available. A total of 20 COI sequences were obtained from Kenya, including records from Baringo, Kilifi, Kisumu, Kwale, Mombasa, and Nairobi. For CYTB, 20 sequences were retrieved from Kenya, mainly from Kilifi and Mombasa. ITS2 was the most limited marker, with 15 sequences in total, comprising six Kenyan sequences and nine additional sequences from Cambodia, Italy, and Sri Lanka. The coastal counties of Mombasa, Kwale, Kilifi, Lamu, Tana River, and Taita Taveta were treated as distinct sampling locations rather than being pooled together. ITS2 sequences for Aedes aegypti were particularly scarce in GenBank, and the limited geographic overlap between ITS2 and the mitochondrial markers should be considered when interpreting the ITS2 phylogenetic results

## 3. Alignment and Trimming

Sequences were aligned using MAFFT with the --auto strategy, and poorly aligned regions were removed with trimAl using the -automated1 option. The resulting alignments differed among genes in length and completeness, reflecting differences in marker variability and sequence availability. CYTB showed the cleanest alignment, with very little missing data, consistent with the narrow geographic origin of the available sequences. COI showed moderate missing data because sequences from different Kenyan counties varied in length. ITS2 showed the highest missing data, largely because globally sourced ITS2 sequences overlapped poorly with the sparse Kenyan records, a limitation that reflects the scarcity of Ae. aegypti ITS2 sequences in GenBank.

## 4. Evolutionary Model Selection

IQ TREE’s ModelFinder was used to select the best fit substitution model for each gene independently using the Bayesian Information Criterion. COI was best fit by HKY+F, CYTB by HKY+F+I, and ITS2 by JC. The HKY based models for COI and CYTB are consistent with mitochondrial loci, where transitions are often more frequent than transversions. The inclusion of an invariant sites parameter for CYTB suggests that a subset of sites was estimated to be highly conserved. ITS2 was assigned the simplest model, likely because the alignment contained relatively few informative sites and substantial missing data, making a more complex model unnecessary under BIC

## 5. Phylogenetic Analysis

### 5.1 Individual Gene Trees (Coalescent Approach)

Maximum likelihood trees were built for each gene independently using IQ-TREE with the best-fit model and 100 standard bootstrap replicates. Bootstrap consensus trees (.contree) were used for visualization and concordance analysis.

**COI gene tree:** Sequences from Kilifi formed a well-supported cluster (bootstrap 93%), and Kisumu sequences grouped together. Nairobi sequences were embedded within the Kilifi cluster, suggesting close relatedness or recent gene flow between coastal and central Kenya populations. Overall bootstrap support was moderate to low at internal nodes, consistent with low genetic divergence within a single species.

**CYTB gene tree:** All 20 sequences were from the Rabai area of Kilifi County, providing essentially no geographic diversity. The tree resolved very little structure, reflecting the expected low variation within a single locality. This severely limits CYTB's contribution to the coalescent species tree.

**ITS2 gene tree:** More variable than the mitochondrial genes, but interpretation is complicated by the inclusion of sequences from Cambodia, Italy, and Sri Lanka. Global sequences were clearly divergent from Kenyan ones, but the Kenyan ITS2 sequences alone were too few to resolve fine-scale population structure.

### 5.2 Coalescent Species Tree (ASTRAL)

ASTRAL combined all three gene trees into a species tree using the unrooted quartet-based coalescent method. The coalescent tree topology was identical to the COI gene tree (Robinson-Foulds distance = 0), reflecting COI's dominance as the most phylogenetically informative marker in this dataset.

### 5.3 Supermatrix Tree (IQ-TREE, Partitioned Analysis)

All three trimmed alignments were concatenated into a supermatrix of 1,301 bp total (COI: positions 1–762, CYTB: 763–1,139, ITS2: 1,140–1,301) using AMAS. A partitioned IQ-TREE analysis was run with gene-specific models (HKY+F for COI, HKY+F+I for CYTB, JC for ITS2) and 100 bootstrap replicates.

**Warning noted:** 37 sequences had >50% gaps in the supermatrix, and 14 sequences failed the composition chi-squared test (p < 0.05). These were predominantly ITS2 sequences and some COI sequences. IQ-TREE proceeded despite these warnings but the results for the supermatrix tree should be interpreted cautiously.

## 6. Tree Comparison

RRobinson Foulds distances quantify topological differences between trees, with a value of 0 indicating identical topology and larger values indicating greater disagreement. In this analysis, COI was identical to the coalescent tree (RF = 0), whereas CYTB and ITS2 showed moderate to substantial topological discordance relative to the coalescent tree. The supermatrix tree showed high RF distances from all three gene trees and also differed substantially from the coalescent tree, indicating strong incongruence among inference approaches. Overall, only one of the three gene trees was fully concordant with the coalescent topology, whereas none matched the supermatrix topology exactly.


## 7. Discussion

### 7.1 Discordance Between Gene Trees

The three gene trees were not fully concordant, indicating substantial topological discordance among markers. Several factors may explain this pattern. First, incomplete lineage sorting is a plausible explanation in a recently diverged species such as Aedes aegypti, where ancestral polymorphisms may persist across lineages. Second, the markers differ in inheritance, evolutionary rate, and selective constraint, with COI and CYTB representing mitochondrial loci and ITS2 representing a nuclear marker with different evolutionary dynamics. Third, the markers differed in geographic coverage, with CYTB sampled only from Rabai, Kilifi, COI sampled more broadly across Kenya, and ITS2 supplemented with global sequences, which may have affected tree resolution and comparability.

### 7.2 Coalescent vs. Supermatrix

The coalescent and supermatrix trees also differed substantially, suggesting that the choice of inference method influenced the recovered topology. This discordance likely reflects both biological signal and data structure. The supermatrix tree should be interpreted cautiously because ITS2 contributed substantial missing data and included geographically distant sequences that were not evenly represented across markers. In contrast, the coalescent approach is better suited to data sets where gene tree discordance is expected, because it combines information across loci without forcing all markers onto a single concatenated topology.

### 7.3 Which Method Is More Reliable?

For this data set, the coalescent analysis appears to provide a more appropriate framework for interpretation. This is mainly because the study focuses on within species population structure, where discordance among loci is expected, and because the available markers differed in sampling completeness and geographic representation. The agreement of COI with the coalescent tree suggests that COI contributed a strong phylogenetic signal in this data set, although the weaker sampling of CYTB and ITS2 likely limited their influence. Taken together, the contrasting trees highlight both the recent evolutionary history of Ae. aegypti and the constraints imposed by uneven marker availability

## 8. Challenges and Limitations

everal limitations should be considered when interpreting these results. First, ITS2 sequences were scarce in GenBank, which required supplementation with globally sourced records and introduced geographic mismatch across loci. Second, CYTB sequences were available only from a single locality, limiting phylogeographic inference for that marker. Third, the low number of parsimony informative sites across loci reduced support for some internal nodes. Finally, the absence of outgroup sequences prevented rooting of the trees, which limits interpretation of evolutionary direction.

## 9. Conclusion

This study reconstructed the phylogenetic relationships of Aedes aegypti from Kenya using three genetic markers and two analytical approaches. The coalescent analysis was the more appropriate framework for this data set because it accommodated marker discordance and reduced the impact of incomplete sampling in individual loci. The supermatrix approach was more vulnerable to the high proportion of missing data in ITS2 and the uneven geographic representation of sequences. Overall, the results show that marker choice, sampling completeness, and method selection all influence the inferred phylogenetic relationships of Aedes aegypti. Future work should include broader Kenyan sampling, additional ITS2 sequences, and outgroup taxa to improve resolution and allow rooted comparisons.


