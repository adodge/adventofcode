#!/usr/bin/env python3
words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
for n in [1,2,3,4,5,6,7,8,9]:
    words[str(n)] = n



import random
import string

def word():
    return random.choice(list(words.keys()))

def junk(n):
    if n == 0: return ""
    while True:
        x = ''.join(random.sample(string.ascii_lowercase, n))
        if not any(w in x for w in words):
            return x
    

def wordjunk(n):
    if n == 0: return ""
    return ''.join(random.sample(string.ascii_lowercase+string.digits, n))

w0,w1 = word(), word()
val = words[w0]*10 + words[w1]

prejunk = random.randint(0,10)
postjunk = random.randint(0,10)
middlejunk = random.randint(0,10)

out = junk(prejunk) + w0 + wordjunk(middlejunk) + w1 + junk(postjunk)

print(val)
print(out)
