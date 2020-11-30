from Bio import SeqIO
from array import *

numseq = 0
countdna = {'A': array('b', []), 'C': array('b', []), 'G': array('b', []), 'T': array('b', [])}
for seqrecord in SeqIO.parse("motif_c.fasta", "fasta"):
    seq = seqrecord.seq
    # print(len(seq))
    count = 0
    if numseq != 0:
        for i in seq:
            countdna[i][count] += 1
            # if i == 'A':
            #     countdna['G'][count] = 0
            #     countdna['C'][count] = 0
            #     countdna['T'][count] = 0
            # elif i == 'C':
            #     countdna['A'][count] = 0
            #     countdna['G'][count] = 0
            #     countdna['T'][count] = 0
            # elif i == 'G':
            #     countdna['A'][count] = 0
            #     countdna['C'][count] = 0
            #     countdna['T'][count] = 0
            # elif i == 'T':
            #     countdna['G'][count] = 0
            #     countdna['C'][count] = 0
            #     countdna['A'][count] = 0
            count = count + 1
        numseq=numseq+1
    else:
        for i in seq:
            countdna[i].append(1)
            if i == 'A':
                countdna['G'].append(0)
                countdna['C'].append(0)
                countdna['T'].append(0)
            elif i == 'C':
                countdna['A'].append(0)
                countdna['G'].append(0)
                countdna['T'].append(0)
            elif i == 'G':
                countdna['A'].append(0)
                countdna['C'].append(0)
                countdna['T'].append(0)
            elif i == 'T':
                countdna['G'].append(0)
                countdna['C'].append(0)
                countdna['A'].append(0)
            # count = count + 1
        numseq=1

string = ""
for j in range(len(countdna['A'])):
    maxg = 0
    maxc = 'A'
    for i in ['A', 'G', 'T', 'C']:
        if countdna[i][j] > maxg:
            maxg = countdna[i][j]
            maxc = i
    string = string + maxc

print("A ", end='')
for i in range(len(countdna['A'])):
    print(countdna['A'][i], end=" ")
print("")
print("C ", end='')
for i in range(len(countdna['C'])):
    print(countdna['C'][i], end=" ")
print("")
print("G ", end='')
for i in range(len(countdna['G'])):
    print(countdna['G'][i], end=" ")
print("")
print("T ", end='')
for i in range(len(countdna['T'])):
    print(countdna['T'][i], end=" ")

print("\n\n" + string)
print(len(string))
print(len(countdna['A']),len(countdna['C']),len(countdna['G']),len(countdna['T']))
print(numseq)
