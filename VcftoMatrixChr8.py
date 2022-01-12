from pysam import VariantFile
import numpy as np
import pandas as pd
from sklearn import decomposition 
vcf_name="ALL.chr8.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf"
panel_name="phase1_integrated_calls.20101123.ALL.panel"

genotypes=[]
samples=[]
variant_ids=[]

#Parse the information in a vcf file (Chromosome 8) with 2183839 samples
with VariantFile(vcf_name) as vcf_reader:
    count=0
    for record in vcf_reader:
        count+=1
        if count%100==0:
            alleles=[record.samples[i].allele_indices for i in record.samples]
            samples=[s for s in record.samples]
            genotypes.append(alleles)
            variant_ids.append(record.id)
        if count%21838==0:
            print(count)
            print(f'{round((count*100)/2183839)} %')
        # if count>=10000:
        #     break
genotypes=np.array(genotypes)

with open(panel_name) as panel:
    labels={} # {sample id: population code}
    for line in panel: # line[0]=sample id, line[1]=population code, line[2]=continents
        line=line.strip().split('\t')
        labels[line[0]]=line[1]
        



#Making a variable to save matrix of genotypes
matrix=np.count_nonzero(genotypes,axis=2)


# Transpose the matrix
matrix=matrix.T

#PCA with 2 components
pca_chr8=decomposition.PCA(n_components=2)
pca_chr8.fit(matrix)
print(pca_chr8.singular_values_)
plot_matrix=pca_chr8.transform(matrix)
print(plot_matrix.shape)

df= pd.DataFrame(matrix, columns=variant_ids, index=samples)
df["Population code"]=df.index.map(labels)
print(df.shape)
df.to_csv("matrix_chr8.csv")


