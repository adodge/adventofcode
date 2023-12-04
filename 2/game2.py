#!/usr/bin/env python3
import sys

z = 0
for line in sys.stdin:
    a,b = line.strip().split(':')
    idx = int(a[5:])

    m = {'red': 0, 'green': 0, 'blue': 0}

    sets = b.split(";")
    for s in sets:
        colors = s.split(',')
        for color in colors:
            n,name = color.strip().split(' ')
            m[name] = max([m[name], int(n)])
    
    z += m['red'] * m['green'] * m['blue']

print(z)
