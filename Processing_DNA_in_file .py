'''
Processing DNA in a file
The file input.txt contains a number of DNA sequences, one per line. Each sequence starts with the same 14 base pair fragment – a sequencing adapter that should have been removed.
 Write a program that will
 trim this adapter and write the cleaned sequences to a new file
print the length of each sequence to the screen.
'''
my_file=open(r"input.txt")
f=my_file.read()
lines=f.split("\n")
seq_line=[]
lenght_line=[]
for line in lines:
    seq_line.append(line[15:])
    lenght_line.append(len(line[15:]))
print(seq_line)
print(lenght_line)