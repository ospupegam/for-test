"""
Restriction fragment lengths
Create a python script in your course project directory called fragment_lengths.py
This script should  calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI
ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
    Hint:
The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk)
"""
dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoRI="GAATTC"
EcoRI_index=dna.find(EcoRI)
seq1=dna[:EcoRI_index+1]
seq2=dna[EcoRI_index+1:]
print(seq1+"\n"+seq2)