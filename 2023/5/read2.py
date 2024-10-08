#!/usr/bin/env python3

import bisect
import sys

ranges = {}
maps = {}

name = None
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    if ':' in line:
        a,b = line.split(':')
        if a[-3:] == 'map':
            src,dst = tuple(a[:-4].split('-to-'))
            maps[src] = {
                'dst': dst,
                'range_start': [],
                'range_size': {},
                'range_offset': {},
            }
            name = src
            continue
        else:
            ranges[a] = []
            xs = list(map(int, b.strip().split()))
            for i in range(0, len(xs), 2):
                ranges[a].append((xs[i],xs[i+1]))
            continue
    
    dst,src,n = map(int, line.strip().split())
    bisect.insort(maps[name]['range_start'], src)
    maps[name]['range_size'][src] = n
    maps[name]['range_offset'][src] = dst-src


def apply(start, length, kind):
    mapdata = maps[kind]
    kind2 = mapdata['dst']
    si = bisect.bisect_right(mapdata['range_start'], start)
    if si > 0:
        s = mapdata['range_start'][si-1]
        assert s <= start
        # rightmost map range starting less than or equal to start
        l = mapdata['range_size'][s]
        d = mapdata['range_offset'][s]
        if start < s+l:
            # start overlaps a map
            overlap = s+l-start
            if overlap >= length:
                return [(start+d, length, kind2)]
            return [
                (start+overlap, length-overlap, kind),
                (start+d, overlap, kind2),
            ]
    # start does not overlap a map
    si = bisect.bisect_left(mapdata['range_start'], start)
    if si != len(mapdata['range_start']):
        s = mapdata['range_start'][si]
        assert s > start
        # leftmost map range starting greater than start
        if start+length-1 > s:
            # we overlap the start of a map
            return [
                (start, s-start, kind2),
                (s, length+start-s, kind),
            ]
            return
    
    # no overlap
    return [(start, length, kind2)]
        
    
stack = [(s,l,'seed') for s,l in ranges['seeds']]

minout = None
while stack:
    s,l,v = stack.pop(-1)
    if v == "location":
        print(f"--- {s}")
        if minout is None or minout > s:
            minout = s
            print(f"!!! {s}")
        continue

    y = apply(s,l,v)
    print(f"{s} {l} {v} ==>")
    for a,b,c in y:
        print(f"\t{a} {b} {c}")
        stack.append((a,b,c))

print(f"=== {minout}")
