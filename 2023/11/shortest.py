#!/usr/bin/env python3

import sys

galaxies = []
for i,line in enumerate(sys.stdin):
    for j,x in enumerate(line.strip()):
        if x == "#":
            galaxies.append((i,j))

n = max(i+1 for i,j in galaxies)
m = max(j+1 for i,j in galaxies)

occ_i = {i for i,j in galaxies}
occ_j = {j for i,j in galaxies}

expansion = 1_000_000-1
z = 0
for k,a in enumerate(galaxies):
    for b in galaxies[k+1:]:
        di = abs(b[0]-a[0])
        di += sum(
            expansion
            for i in range(min(a[0], b[0])+1, max(a[0],b[0]))
            if i not in occ_i
        )
        dj = abs(b[1]-a[1])
        dj += sum(
            expansion
            for j in range(min(a[1], b[1])+1, max(a[1],b[1]))
            if j not in occ_j
        )
        d = di+dj
        z += d
        print(a,b,d)
print(z)
