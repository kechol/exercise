#!/usr/bin/env python

from copy import deepcopy

cs = [[]*8]*8
qs = []


def fill(cs, q):
    for i in range(8):
        cs[q[0]][i] = 'X'
        cs[i][q[1]] = 'X'

        p = q[0] + q[1] - i
        if p > -1 and p < 8:
            cs[i][p] = 'X'

        p = q[0] - q[1] + i
        if p > -1 and p < 8:
            cs[p][i] = 'X'

    cs[q[0]][q[1]] = 'Q'


def check(cs):
    for i in range(8):
        if '.' not in cs[i] and 'Q' not in cs[i]:
            return False
    return True


def loop(i, cs):
    if i == 8 and len(qs) == 8:
        print("\n".join(["".join(c) for c in cs]))
        exit()

    if 'Q' in cs[i]:
        loop(i+1, cs)

    cst = deepcopy(cs)

    for j in range(8):
        if cs[i][j] == '.':
            fill(cs, [i, j])
            if check(cs):
                # add Q to map
                qs.append([i, j])
                loop(i+1, cs)
            else:
                # revert map
                cs = cst


# init map
for i in range(8):
    cs[i] = list(input())
    if 'Q' in cs[i]:
        q = [i, cs[i].index('Q')]
        qs.append(q)


# fill map for three of first Qs
for q in qs:
    fill(cs, q)


# join the loop
loop(0, cs)
print("No Answer")
