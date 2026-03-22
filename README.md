# B13 Comparative Genomics Analysis

This repository contains the comparative genomics analysis workflow and results for the bacterial strain B13. The project encompasses pangenome analysis, identification of mobile genetic elements (MGEs), and functional annotation of genes related to environmental adaptation.

## Directory Structure

### [01.Pangenome_analysis_full/](./01.Pangenome_analysis_full/)
Focuses on the core and accessory genome analysis.
- `01.Prokka/`: Genome annotation results used as input for the pangenome pipeline.
- `02.Roary/`: Roary output files and gene presence/absence matrices.
- `metadata.jsonl` and `metadata.tsv`: Metadata for all genome in pangenome analysis
- `Convert_jsonl_to_tsv.py`: Custom scripts for processing pangenome metadata.

### [Pangenome_plot/](./Pangenome_plot/)
Visualization and classification of pangenome components.
- `roary/`: Detailed plots (pie charts, distribution plots) generated from Roary results.
- `COG_classifier/`: Functional classification of the pangenome using Clusters of Orthologous Groups.
- `Visualization.py`: Main script for generating pangenome-related figures.

### 3. [CRISPR-Cas_system/](./CRISPR-Cas_system/)
Identification and characterization of immune systems.
- `CasFinder_res/` & `macsyfinder/`: Raw outputs from Cas-system detection tools.
- `CRISPR-Cas_system.report.md`: Summary report of detected CRISPR arrays and Cas proteins.
- Contains B13 genome and protein sequences used for the search.

### 4. [GenomeIsland_PathogenecityIsland_HGT/](./GenomeIsland_PathogenecityIsland_HGT/)
Analysis of horizontal gene transfer and genomic islands (GIs).
- `GenomicIslandPrediction/` & `B13_treasuraisland/`: Results from GI prediction algorithms.
- `VF_results.tsv`: Identification of virulence factors within the genome.
- `GenomeIsland_PathogenecityIsland_HGT.report.md`: Integrated analysis of MGEs and pathogenicity potential.

### 5. [Predict_Stress_Response_Environmental_Adaptation_Genes/](./Predict_Stress_Response_Environmental_Adaptation_Genes/)
Functional profiling for environmental fitness.
- `B13_eggnog/` / `B13_kofamscan/`: Functional annotations using EggNOG-mapper and KofamScan.
- `B13_COG.eggnog.filtered.tsv`: Curated list of genes involved in stress response.
- `Predict_Stress_Response_Environmental_Adaptation_Genes.md`: Detailed report on genes contributing to stress tolerance and adaptation.

## Methodology & Tools
- **Annotation:** Prokka, EggNOG-mapper, KofamScan.
- **Pangenomics:** Roary.
- **Defense Systems:** CasFinder, MacSyFinder.
- **MGEs:** TreasureIsland, Proksee.
- **Data Processing:** Python (Pandas, Matplotlib, Seaborn).

---
*Project maintained by Dat Nguyen.*
