#!/usr/bin/env python3

import subprocess
import sys


program = sys.argv[1]
testgen = sys.argv[2]

while True:
    p = subprocess.run([testgen], capture_output=True)
    exp,test = p.stdout.split(b'\n', 1)
    exp = int(exp)

    print(test, exp)

    p = subprocess.run([program], input=test, capture_output=True)

    if p.returncode != 0:
        print("failed")
        sys.exit(1)

    output = int(p.stdout)
    if output == exp:
        continue

    print("failed")
    sys.exit(1)
