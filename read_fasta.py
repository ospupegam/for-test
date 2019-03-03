"""
Writing a FASTA file
Write a program that will create a FASTA file for the following three sequences
Make sure that all sequences are in upper case and only contain the bases A, T, G and C.
Hint:
FASTA file format is a commonly-used DNA and protein sequence file format. A single sequence in FASTA format looks like this:
>sequence_name
ATCGACTGATCGATCGTACGAT
"""
my_file=open("out_fasta.txt","w")
seq1_header=">sequence_one"
seq1_seq="ATCGATCGATCGATCGNNNNNNNAT"
seq1_seq=seq1_seq.replace("N","")
my_file.write(seq1_header)
my_file.write("\n")
my_file.write(seq1_seq.upper())
