#!/usr/bin/env python3.11
import sys

for line in sys.stdin:
    dat0,ns0 = line.strip().split(' ')
    ns0 = list(map(int, ns0.split(',')))

    unknown = [(dat0, tuple(ns0))]
    fixed = []

    while unknown:
        dat, ns = unknown.pop(-1)
        
        
