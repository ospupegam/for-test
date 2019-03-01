dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoRI="GAATTC"
EcoRI_index=dna.find(EcoRI)
seq1=dna[:EcoRI_index+1]
seq2=dna[EcoRI_index+1:]
print(seq1+"\n"+seq2)