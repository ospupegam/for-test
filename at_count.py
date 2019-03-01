"""
Create a python script in your course project directory called ae_content.py
This script should print the AT content of this short DNA sequence
ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
    Hint:
AT content of a sequence is the number of A & T bases divided by the total number of bases.
"""
dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a=dna.upper().count("A")
t=dna.upper().count("T")
c=dna.upper().count("C")
g=dna.upper().count("G")
at=(a+t)/(a+t+c+g)
print(at)