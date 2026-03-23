# B13 Comparative Genomics Analysis

This repository contains the comparative genomics analysis workflow and results for the bacterial strain B13. The project encompasses pangenome analysis, identification of mobile genetic elements (MGEs), and functional annotation of genes related to environmental adaptation.

## Directory Structure

### [01.Pangenome_analysis_full/](./01.Pangenome_analysis_full/)
Focuses on the core and accessory genome analysis of the complete set of samples.
- `01.Prokka/`: Genome annotation results (.gff) used as input for the pangenome pipeline.
- `02.Roary/`: Roary output files including gene presence/absence matrices, core/accessory alignments, and summary plots.
- `metadata.jsonl` and `metadata.tsv`: Metadata for all genomes in pangenome analysis.
- `Convert_jsonl_to_tsv.py`: Custom script for processing pangenome metadata.

### [02.Pangenome_analysis_20samples/](./02.Pangenome_analysis_20samples/)
Pangenome analysis focused on a subset of 20 samples.
- `01.Genome_data/`: Input fasta files for the selected samples.
- `02.Annotated_data/`: Annotated gff files.
- `03.Roary_data/`: Roary analysis results for this subset.

### [03.CRISPR-Cas_system_analysis/](./03.CRISPR-Cas_system_analysis/)
Identification and characterization of immune systems in strain B13.
- `01.B13_annotated_data/`: B13 genome and protein sequences.
- `02.B13_CasFinder_results/`: Results from CasFinder, including detected systems and candidates.

### [04.GenomeIsland_analysis/](./04.GenomeIsland_analysis/)
Analysis of horizontal gene transfer and genomic islands (GIs) for strain B13.
- `02.B13_TreasuraIsland_data/`: Results from GI prediction algorithms.
- `03.B13_IslandViewer_data/`: Genomic island predictions from IslandViewer.
- `05.B13_Virulence_Factors/`: Identification of virulence factors.
- `GenomeIsland_PathogenecityIsland_HGT.report.md`: Integrated analysis of MGEs and pathogenicity potential.

### [05.Stress_response_environmental_adaptation_genes_analysis/](./05.Stress_response_environmental_adaptation_genes_analysis/)
Functional profiling for environmental fitness of strain B13.
- `02.B13_emapper_data/`: Functional annotations using EggNOG-mapper.
- `03.B13_COG_data/`: COG classification results and distribution plots.
- `04.B13_GO_data/`: Gene Ontology analysis and visualizations.
- `05.B13_KEGG_data/`: KEGG pathway mapping and analysis results.
- `Predict_Stress_Response_Environmental_Adaptation_Genes.md`: Detailed report on genes contributing to stress tolerance and adaptation.

## Methodology & Tools
- **Annotation:** Prokka, EggNOG-mapper, KofamScan.
- **Pangenomics:** Roary.
- **Defense Systems:** CasFinder, MacSyFinder.
- **MGEs:** TreasureIsland, IslandViewer, VFDB.
- **Data Processing:** Python (Pandas, Matplotlib, Seaborn).

---
*Project maintained by Dat Nguyen.*
