# PET-project-1-Chr8Variants
## Background
- Variant identifier files (VCF) have all the SNP sites from 1000Genome with samples.
- Samples have IDs that connect to the (super)population information.

## Methods
- Download Chromosome8 VCF file.
- The VCF file has rows with SNPs and Columns with positions, Ids, reference/altered sequences and samples, each row has information about the variant
![chr8_vcf](https://user-images.githubusercontent.com/54334941/149042219-ad05ef60-14f3-47ec-b774-df4516c12fcc.png)
- Information about each sample
![vcf2](https://user-images.githubusercontent.com/54334941/149042499-17976057-686d-4961-9ace-f084fd30ca49.png)
- VCF to matrix : Making matrix (rows with samples) *VcftoMatrixChr8.py
- Dimensionality reduction with PCA (Linear) & t-SNE (Non linear)
  - __PCA__
  
  ![PCA](https://user-images.githubusercontent.com/54334941/149052633-41ae4dcf-323c-440a-b156-1111abbfef87.png)
  
  - __t-SNE__
  
  ![t-SNE](https://user-images.githubusercontent.com/54334941/149052638-454f3ba1-795f-40a7-b461-7913f7dfe01b.png)

## Future studies
- Analyzing t-SNE
  - Modifying the matrix format
- Analyzing specific variants on specific genes
  - Myc and PVT1 believed to be involved in oncogenic/tumor suppressor mechanisms are on Chr8
    - Myc and PVT1 are related to prostate cancer, which has different portion between superpopulation group (African >> other groups)
