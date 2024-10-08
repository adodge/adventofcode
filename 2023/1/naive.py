#!/usr/bin/env python3
words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
for n in [0,1,2,3,4,5,6,7,8,9]:
    words[str(n)] = n

import sys

for line in sys.stdin:
    first_word = None
    first_word_index = None
    last_word = None
    last_word_index = None
    for w in words:
        if w not in line: continue
        i = line.index(w)
        if first_word_index is None or first_word_index > i:
            first_word = w
            first_word_index = i
        i = line.rindex(w)
        if last_word_index is None or last_word_index < i:
            last_word = w
            last_word_index = i

    
