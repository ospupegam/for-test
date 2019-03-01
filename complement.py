"""
Complementing DNA
Create a python script in your course project directory called complement_dna.py
This script should print the AT content of this short DNA sequence
ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
    Hint:
A DNA molecule is a double stranded sequence of bases in which every strand is a complement of the other. There are bonds between the bases of both strands in which A always binds T and C always binds G.
"""
dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_1=dna.replace("A","t")
dna_2=dna_1.replace("C","g")
dna_3=dna_2.replace("T","a")
dna_4=dna_3.replace("G","c").upper()
print(dna+"\n"+dna_4)
