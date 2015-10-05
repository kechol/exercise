#!/usr/bin/env python

import sys


class TaroHeikinchi:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = 0
        self.m = 0

    def solve(self):
        xpy = self.x / self.y

        if xpy < 1:
            return False

        sm = 0
        for i in range(1, self.x + 1):
            sm += i
            # print('i', i, 'sm', sm)
            if (sm / i) - 1 > xpy:
                self.n = i
                break

        for i in range(self.n, 0, -1):
            sm = sum(range(i+1))

            if sm / i - 1 > xpy:
                continue

            for j in range(i, 0, -1):
                r = (sm - j) / i
                # print('n', i, 'm', j, 'r', r)
                if r == xpy:
                    self.n = i
                    self.m = j
                    return True

        return False


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    x, y = [int(i) for i in input().split('/')]
    th = TaroHeikinchi(x, y)
    if th.solve():
        print(th.n, th.m)
    else:
        print('Impossible')
