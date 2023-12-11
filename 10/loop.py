#!/usr/bin/env python3.11

import sys

X = {}
start = None
for i,row in enumerate(sys.stdin):
    for j,cell in enumerate(row.strip()):
        if cell == "S":
            start = i,j
        X[i,j] = cell

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
    history = []
    while True:
        history.append(state[0])
        cell = X[state[0]]
        if cell not in celltypes:
            break
        if state[1] not in celltypes[cell]:
            break
        d = celltypes[cell][state[1]]
        state = (move(state[0], d), d)

    if state[0] == start:
        print(len(history)//2)
        break
