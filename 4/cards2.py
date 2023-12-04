#!/usr/bin/env python3
import sys
from collections import defaultdict

z = 0
extra_copies = defaultdict(int)

for i,line in enumerate(sys.stdin):
    n = extra_copies[i]
    z += n+1
    print(i, n+1, z)

    _,b = line.strip().split(':')
    have,winning = [x.strip().split() for x in b.split("|")]
    overlap = len(set(have).intersection(set(winning)))
    for j in range(overlap):
        extra_copies[i+j+1] += n+1
    print(extra_copies)

print(z)
