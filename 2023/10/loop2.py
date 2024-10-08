#!/usr/bin/env python3.11

import sys

X = {}
start = None
for i,row in enumerate(sys.stdin):
    for j,cell in enumerate(row.strip()):
        if cell == "S":
            start = i,j
        X[i,j] = cell
n_rows = max(i for i,j in X)+1
n_cols = max(j for i,j in X)+1

celltypes = {
    "|": {"N": "N", "S": "S"},
    "-": {"W": "W", "E": "E"},
    "L": {"S": "E", "W": "N"},
    "J": {"S": "W", "E": "N"},
    "7": {"E": "S", "N": "W"},
    "F": {"W": "S", "N": "E"},
}

def move(cell, direction):
    if direction == "W":
        return (cell[0],cell[1]-1)
    if direction == "E":
        return (cell[0],cell[1]+1)
    if direction == "N":
        return (cell[0]-1,cell[1])
    if direction == "S":
        return (cell[0]+1,cell[1])
    raise RuntimeError

for d in "NSEW":
    state = (move(start, d), d)
    enters = {}
    exits = {start: d}
    while True:
        enters[state[0]] = state[1]
        cell = X[state[0]]
        if cell not in celltypes:
            break
        if state[1] not in celltypes[cell]:
            break
        d = celltypes[cell][state[1]]
        exits[state[0]] = d
        state = (move(state[0], d), d)

    if state[0] == start:
        break


n = 0
for i in range(n_rows):
    print("Row", i)
    above, below = 0,0
    for j in range(n_cols):
        if (i,j) not in enters:
            if above != 0 and below != 0:
                n += 1
            print(n,i,j," ", " ", " ", above, below)
            continue
        en,ex = enters[i,j], exits[i,j]
        c = X[i,j]
        
        if en == "N":
            below -= 1
        elif en == "S":
            above -= 1
        
        if ex == "N":
            above += 1
        elif ex == "S":
            below += 1

        print(n,i,j,c,en,ex,above,below)
        
    print()

print(n)
