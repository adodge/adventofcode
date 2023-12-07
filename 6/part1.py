#!/usr/bin/env python3
import sys
from math import sqrt,ceil,floor

vecs = {}
for line in sys.stdin:
    name,vals = line.split(":")
    vecs[name] = list(map(int,vals.strip().split()))


p = 1
for time,target in zip(vecs['Time'], vecs['Distance']):
    a,b,c = -1, time, -target

    disc = b*b - 4*a*c

    x = (-b + sqrt(disc)) / 2 / a

    xb = ceil(x)
    if x == xb:
        xb = xb+1

    ans = 1+time - xb*2
    print(ans)
    p *= ans

print("!", p)
