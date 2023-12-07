#!/usr/bin/env python3

import bisect
import sys

sets = {}
maps = {}
paths = {}

map_pair= None
for line in sys.stdin:
    line = line.strip()
    if not line:
        map_pair = None
        continue

    if ':' in line:
        a,b = line.split(':')
        if a[-3:] == 'map':
            map_pair = tuple(a[:-4].split('-to-'))
            maps[map_pair] = {
                'start': [],
                'map': {},
            }
            paths[map_pair[0]] = map_pair[1]
            continue
        else:
            sets[a] = set(map(int, b.strip().split()))
            map_pair = None
            continue
    
    assert map_pair is not None

    dst,src,n = map(int, line.strip().split())
    bisect.insort(maps[map_pair]['start'], src)
    maps[map_pair]['map'][src] = (dst, n)


out = set()
for x in sets['seeds']:
    v = 'seed'
    while v != 'location':
        v1 = paths[v]
        src_idx = bisect.bisect_right(maps[v,v1]['start'], x)
        if src_idx > 0:
            src = maps[v,v1]['start'][src_idx-1]
            dst,n = maps[v,v1]['map'][src]
            if x < src+n:
                y = x + dst - src
                print(f' {v} {x} => {v1} {y}')
                x,v = y,v1
                continue
        print(f'*{v} {x} => {v1} {x}')
        v = v1
        continue
    out.add(x)
    print()
    

print(min(out))
