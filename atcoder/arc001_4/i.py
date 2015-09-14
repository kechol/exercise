#/usr/bin/env python

import random


n = random.randint(150000, 200000)
s = 0
g = 0
lrs = []

for i in range(n):
    l = random.randint(0, 999999)
    r = random.randint(l, 1000000)
    lrs.append([l, r])
    if i == 0:
      s = random.randint(l, r)
    if i == n - 1:
      g = random.randint(l, r)

print(n)
print("{0} {1}".format(s, g))
for i in range(n):
  print("{0} {1}".format(lrs[i][0], lrs[i][1]))
