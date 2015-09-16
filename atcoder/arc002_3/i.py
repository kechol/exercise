#!/usr/bin/env python

import random

n = 999
cmd = ""
cmds = ['A', 'B', 'X', 'Y']
for i in range(n):
    cmd += cmds[random.randint(0, 3)]

print(n)
print(cmd)
