# PET-project-1-Chr8Variants
## Background
- Variant identifier files (VCF) have all the SNP sites from 1000Genome with samples.
- Samples have IDs that connect to the (super)population information.
- Prostate cancer has disproportional impacts on African-ancestry (at about twice, compare to European ancestry). *
- Prostate cancer diagnosis/progression is highly related to PVT1, which is on Chromosome8, and PVT1 exon 4A and 4B are highly involved in the disproportion. **
- Compare samples of the SNP sites on PVT1 (or other oncogenic locus) between superpopulation groups.

## Methods
- Download Chromosome8 VCF file.
- The VCF file has rows with SNPs and Columns with positions, Ids, reference/altered sequences and samples, each row has information about the variant
![chr8_vcf](https://user-images.githubusercontent.com/54334941/149042219-ad05ef60-14f3-47ec-b774-df4516c12fcc.png)
- Information about each sample
![vcf2](https://user-images.githubusercontent.com/54334941/149042499-17976057-686d-4961-9ace-f084fd30ca49.png)
-  




## References

\* Lewis DD, Cropp CD. The Impact of African Ancestry on Prostate Cancer Disparities in the Era of Precision Medicine. Genes (Basel). 2020 Dec 8;11(12):1471. doi: 10.3390/genes11121471. PMID: 33302594; PMCID: PMC7762993.

** Pal G, Di L, Orunmuyi A, Olapade-Olaopa EO, Qiu W, Ogunwobi OO. Population Differentiation at the PVT1 Gene Locus: Implications for Prostate Cancer. G3 (Bethesda). 2020 Jul 7;10(7):2257-2264. doi: 10.1534/g3.120.401291. PMID: 32358016; PMCID: PMC7341130.
