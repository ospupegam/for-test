"""
Splicing out introns, part one
Create a python script in your course project directory called introns1.py
This script should print just the coding regions of the DNA sequence
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACT ACTAT
    Hint:
The sequence comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence
"""
dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACT ACTAT"
exon1=dna[:63]
exon2=dna[91:]
intron=dna[63:91]
if len(dna)==(len(exon1)+len(exon2)+len(intron)):
    print("true")
