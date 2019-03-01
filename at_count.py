dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a=dna.upper().count("A")
t=dna.upper().count("T")
c=dna.upper().count("C")
g=dna.upper().count("G")
at=(a+t)/(a+t+c+g)
print(at)