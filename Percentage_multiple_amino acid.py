def multi_amino_acid_residue_percentage(amino_acid,residue=["A", "I", "L", "M", "F", "W","Y" , 'V']):
    print("you enter amino acid : " + amino_acid)
    print("you enter residue : " ,residue)
    amino_acid_residue=[]
    for elem in range(len(residue)):
        amino_acid_residue.append(amino_acid.upper().count(residue[elem].upper()))
    result=(sum(amino_acid_residue)/len(amino_acid))*100
    print(int(result))
    return int(result)

assert multi_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])==5
assert multi_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert multi_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert multi_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP") == 65
