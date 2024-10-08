#!/usr/bin/env python3

import sys
from collections import Counter

cardvalue = {x: i for i,x in enumerate("J23456789TQKA")}

ranked_hands = []

for line in sys.stdin:
    hand, bid = line.strip().split(' ')
    bid = int(bid)
    c = Counter(Counter([x for x in hand if x != "J"]).values())
    n_jokers = len([x for x in hand if x == "J"])
    score = [c[i] for i in [5,4,3,2,1]]
    best = min([i for i,n in enumerate(score) if n > 0]+[5])
    if best < len(score):
        score[best] -= 1
    score[best-n_jokers] += 1
    rankby = (tuple(score), tuple(map(lambda x: cardvalue[x], hand)))

    print(hand, bid, rankby)
    
    ranked_hands.append((rankby, hand, bid))

ranked_hands.sort()

z = 0
for mult, (_, _, bid) in enumerate(ranked_hands):
    z += (mult+1) * bid

print(z)
