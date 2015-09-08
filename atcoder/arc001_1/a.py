#!/usr/bin/env python

n = input()
cs = input()
cnt = [0]*4

for c in cs:
    cnt[int(c)-1] += 1

print("{} {}".format(max(cnt), min(cnt)))