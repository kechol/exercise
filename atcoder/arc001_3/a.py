#!/usr/bin/env python

cs = [[]*8]*8
qs = []

for i in range(0, 7):
    cs[i] = list(input())
    if 'Q' in cs[i]:
        qs.append([i, cs[i].index('Q')])


print("\n".join(["".join(c) for c in cs]))

for q in qs:
    for i in range(0, 7):
        cs[q[0]][i] = 'X'
        cs[i][q[1]] = 'X'
        p = q[0] + q[1]
        if p - i < 8:
            cs[i][p-i] = 'X'
        p = abs(q[0] - q[1])
        if p + i < 8:
            cs[i][p+i] = 'X'

    print("\n".join(["".join(c) for c in cs]))