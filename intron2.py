
"""
Splicing out introns, part two
Create a python script in your course project directory called introns2.py
This script should  calculate what percentage of the DNA sequence is coding
"""
dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACT ACTAT"
exon1=dna[:63]
exon2=dna[91:]
intron=dna[63:91]
dna_coding_per=(len(exon1)+len(exon2))/((len(exon1)+len(exon2))+len(intron))
print(dna_coding_per)