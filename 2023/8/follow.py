#!/usr/bin/env python3.11
import sys
import math

steps = sys.stdin.readline().strip()
step_size = len(steps)

sys.stdin.readline()

rawnodes = {}
for line in sys.stdin:
    a,b = line.strip().split(' = ')
    l,r = b[1:-1].split(', ')
    rawnodes[a] = {"L": l, "R": r}

nodes = {}
for node in rawnodes:
    node1 = node
    for step in steps:
        node1 = rawnodes[node1][step]
    nodes[node] = node1

del rawnodes

node_characteristics = {}
def characterize_node(node):
    history = []
    seen = set()
    node1 = node
    while node1 not in seen:
        history.append(node1)
        seen.add(node1)

        node1 = nodes[node1]
    
    time_to_cycle = history.index(node1)
    cycle_length = len(history) - time_to_cycle
    
    node_characteristics[node] = [time_to_cycle, cycle_length, history]

for node in nodes:
    characterize_node(node)

states = {x for x in nodes if x[-1] == "A"}

n_steps = 0

cycles = []

while any(n[-1] != 'Z' for n in states):
    print(n_steps, states)
    if any(node_characteristics[n][0] != 0 for n in states):
        states = {nodes[s] for s in states}
        n_steps += 1
    else:
        for n in states:
            _,cycle_length,history = node_characteristics[n]
            cycles.append([cycle_length, {i for i,x in enumerate(history) if x[-1] == 'Z'}])
        break

while len(cycles) > 1:
    cycles.sort()
    a,aidxs = cycles.pop(0)
    b,bidxs = cycles.pop(0)
    print(a,aidxs, b,bidxs)
    out = math.lcm(a,b)
    out_idxs = set()

    length_diff = b-a
    for aidx in aidxs:
        for bidx in bidxs:
            steps = min([aidx, bidx])
            aidx -= steps
            bidx -= steps
            while aidx != bidx:
                steps += a
                bidx = (bidx+length_diff) % b
            out_idxs.add(steps)

    print(out, out_idxs)
    cycles.append([out, out_idxs])

print((n_steps + min(cycles[0][1]))*step_size)
