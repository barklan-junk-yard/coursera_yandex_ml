import re
import scipy.spatial
import os
from numpy import zeros

def countOccurences(a, word): 
    count = 0
    for i in a: 
        if (word == i): 
           count += 1
    return count

with open('YA_ML/sentences.txt', 'r') as infile:
    lst = []
    n = 0
    for line in infile:
        n += 1
        temp = line.strip().lower()
        p = re.compile(r"[^a-z]+")
        lst += p.split(temp)
    while '' in lst:
        lst.remove('')
wordsdict = {}
index = 0
for word in lst:
    if word not in wordsdict:
        wordsdict[word] = index
        index += 1
d = len(wordsdict)
main = zeros((n, d))
with open('YA_ML/sentences.txt', 'r') as infile:
    i = 0
    for line in infile:
        p = re.compile(r"[^a-z]+")
        temps0 = line.strip().lower()
        temps = p.split(temps0)
        j = 0
        for tempw in wordsdict:
            tmp1 = countOccurences(temps, tempw)
            main[i, j] = tmp1
            j += 1
        i += 1

dist = {}
for i in range(1, n):
    dist[i] = scipy.spatial.distance.cosine(main[0], main[i])
distsr = {k: v for k, v in sorted(dist.items(), key=lambda item: item[1])}
outstr = str(list(distsr.keys())[0]) + " " + str(list(distsr.keys())[1])
outstr = outstr.strip()
print(outstr)
with open('YA_ML/outfile.txt', 'w', newline='') as outfile:
    outfile.write(outstr)
