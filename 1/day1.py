import sys
acc = 0
for line in sys.stdin:
    digits = [c for c in line if c in "0123456789"]
    if not digits: continue
    print(acc, digits[0], 10)
    acc += int(digits[0])*10
    print(acc, digits[-1], 1)
    acc += int(digits[-1])
print(acc)
