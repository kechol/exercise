#!/usr/bin/env python

import sys
import math


class TaroHeikinchi:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rs = []

    def solve(self):
        xpy = self.x / self.y
        tn = 2 * xpy

        if tn < 1:
            return False

        for n in range(math.floor(tn) - 1, math.ceil(tn) + 2):
            if n % self.y > 0:
                continue

            sm = n * (n + 1) / 2
            m = sm - n * xpy

            # print('n', n, 'm', m, 'sm', sm)

            if m < 1:
                continue

            self.rs.append((int(n), int(m)))

        return len(self.rs) > 0


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    x, y = [int(i) for i in input().split('/')]
    th = TaroHeikinchi(x, y)
    if th.solve():
        for r in th.rs:
            print(r[0], r[1])
    else:
        print('Impossible')
