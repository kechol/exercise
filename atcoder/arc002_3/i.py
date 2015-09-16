#!/usr/bin/env python

import random

n = 1000
# n = 999
cmd = ""
# cmds = ['A', 'B', 'X', 'Y']
cmds = ['A', 'B']
for i in range(n):
    cmd += cmds[random.randint(0, len(cmds)-1)]

print(n)
print(cmd)
