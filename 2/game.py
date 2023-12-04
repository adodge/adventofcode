#!/usr/bin/env python3
import sys

limit = {'red': 12, 'green': 13, 'blue': 14}
z = 0

for line in sys.stdin:
    a,b = line.strip().split(':')
    idx = int(a[5:])

    possible = True

    sets = b.split(";")
    for s in sets:
        colors = s.split(',')
        for color in colors:
            n,name = color.strip().split(' ')
            if name not in limit:
                possible = False
                break
            if int(n) > limit[name]:
                possible = False
                break
    if possible:
        z += idx

print(z)
