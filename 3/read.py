#!/usr/bin/env python3
import sys
import string

symbols = set()
numbers = set()

for i,row in enumerate(sys.stdin):
    num_start = None
    acc = []
    for j,x in enumerate(row.rstrip()):
        if x in string.digits:
            if num_start is None:
                num_start = j
            acc.append(x)
        else:
            if acc:
                numbers.add( (i, num_start, tuple(acc)) )
                num_start = None
                acc = []
            
            if x == ".":
                continue
            
            symbols.add( (i,j) )

    if acc:
        numbers.add( (i, num_start, tuple(acc)) )
        acc = []

part_nums = []
for i,j,num in numbers:
    to_check = set()
    l = len(num)
    if j > 0:
        to_check.add((i,j-1))
    to_check.add((i,j+l))
    for b in range(max([0,j-1]), j+l+1):
        if b < 0:
            continue
        if i > 0:
            to_check.add((i-1, b))
        to_check.add((i+1, b))
    
    if any(c in symbols for c in to_check):
        part_nums.append(int(''.join(num)))

print(sum(part_nums))
