"""
The file genomic_dna.txt contains a section of genomic DNA, and the file exons.txt contains a list of start/stop positions of exons. Each exon is on a separate line and the start and stop positions are separated by a comma.
 Write a program that will extract the exon segments, concatenate them, and write them to a new file.
"""
my_genomic=open("genomic_dna.txt")
g=my_genomic.read()
my_exon=open("exon.txt")
e=my_exon.read()
r=e.split("\n")
e_list=[]
for elem in r:
    e_list.append(elem.split(","))
g_list=[]
for j in range(len(e_list)):
    g_list.append(g[int(e_list[j][0]):int(e_list[j][1])])
print(g_list)