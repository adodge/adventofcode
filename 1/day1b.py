#!/usr/bin/env python3
import sys

words = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine",
]

acc = 0
for line in sys.stdin:
    word_state = [0]*9
    last_digit = None
    def handle_digit(x):
        global last_digit,acc,word_state
        if last_digit is None:
            acc += 10*x
        last_digit = x

    for c in line:
        if c in "123456789":
            handle_digit(int(c))
            continue
        for i,word in enumerate(words):
            if c == word[word_state[i]]:
                word_state[i] += 1       
                if word_state[i] == len(word):
                    handle_digit(i+1)
                    word_state[i] = 0
            elif c == word[0]:
                word_state[i] = 1
            else:
                word_state[i] = 0
    
    acc += last_digit    

print(acc)
