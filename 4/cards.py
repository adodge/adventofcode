#!/usr/bin/env python3
import sys

z = 0
for line in sys.stdin:
    _,b = line.strip().split(':')
    have,winning = [x.strip().split() for x in b.split("|")]
    overlap = set(have).intersection(set(winning))
    if not overlap: continue
    value = 2**(len(overlap)-1)
    z += value

print(z)
