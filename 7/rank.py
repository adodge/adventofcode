#!/usr/bin/env python3

import sys
from collections import Counter

cardvalue = {x: i for i,x in enumerate("23456789TJQKA")}

ranked_hands = []

for line in sys.stdin:
    hand, bid = line.strip().split(' ')
    bid = int(bid)
    c = Counter(Counter(hand).values())
    score = [c[i] for i in [5,4,3,2,1]]
    rankby = (tuple(score), tuple(map(lambda x: cardvalue[x], hand)))
    
    ranked_hands.append((rankby, hand, bid))

ranked_hands.sort()

z = 0
for mult, (_, _, bid) in enumerate(ranked_hands):
    z += (mult+1) * bid

print(z)
