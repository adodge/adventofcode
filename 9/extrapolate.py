#!/usr/bin/env python3

import sys

xs = []
for line in sys.stdin:
    xs.append(list(map(int, line.strip().split())))

def extrapolate(xx):
    if all(x == 0 for x in xx):
        return 0

    yy = [xx[i]-xx[i-1] for i in range(1,len(xx))]
    d = extrapolate(yy)
    return xx[-1] + d

def rextrapolate(xx):
    if all(x == 0 for x in xx):
        return 0

    yy = [xx[i]-xx[i-1] for i in range(1,len(xx))]
    d = rextrapolate(yy)
    return xx[0] - d

z,rz = 0,0
for x in xs:
    y = extrapolate(x)
    ry = rextrapolate(x)
    print(x,y,ry)
    z += y
    rz += ry
print(z,rz)
