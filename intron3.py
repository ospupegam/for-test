"""
plicing out introns, part two
Create a python script in your course project directory called introns3.py
This script should print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase
"""
dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACT ACTAT"
exon1=dna[:63]
exon2=dna[91:]
intron=dna[63:91]
dna_coding_per=(len(exon1)+len(exon2))/((len(exon1)+len(exon2))+len(intron))
dna_coding=exon1+exon2
dna_noncoding=intron
print("dna coding: " + dna_coding + "\n" + "dna noncoding : " +dna_noncoding )