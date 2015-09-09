#!/usr/bin/env python

"""
1=1+
2=1+1+
3=5+1-1-
4=5+1-
5=5+
6=5+1+
7=5+1+1+
8=10+1-1-
9=10+1-
"""

i = input().split(' ')
a = int(i[0])
b = int(i[1])
cnt = 0
gap = abs(b - a)

cnt += gap // 10
gap %= 10

rem = gap % 5
if(rem > 2):
    rem = 5 - rem

cnt += rem

if(gap > 2):
    cnt += 1

print(cnt)
