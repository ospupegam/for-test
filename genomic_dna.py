"""
Splitting genomic DNA
In materials folder, there is a file called genomic_dna.txt
 Write a program that will split the genomic DNA into coding and non-coding parts, and write these sequences to two separate files
"""
dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACT ACTAT"
exon1=dna[:63]
exon2=dna[91:]
intron=dna[63:91]
dna_coding_per=(len(exon1)+len(exon2))/((len(exon1)+len(exon2))+len(intron))
dna_coding=exon1+exon2
dna_noncoding=intron
my_file=open("out_file.txt","w")
my_file.write(dna_coding)
my_file.write("\n")
my_file.write(dna_noncoding)
my_file.close()