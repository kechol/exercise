#!/usr/bin/env python

import sys


class DarkWayHome:

    def __init__(self, n, m, cs):
        self.n = n
        self.m = m
        self.cs = cs
        self.light = 10.0
        self.goal = False

        sp = self.start_point()
        self.move(sp, 0, 9)

    def start_point(self):
        for i in range(self.n):
            if 's' in self.cs[i]:
                return [i, self.cs[i].index('s')]

    def move(self, p, t, n):
        if n < 1:
            return

        if t > 0:
            tl = float(self.cs[p[0]][p[1]]) * (0.99 ** t)
            if tl < self.light:
                self.light = tl

        # print("\n".join(["".join(c) for c in self.cs]), "\n", t, n, self.light, "\n")

        ds = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        for i, d in enumerate(ds):
            np = [p[0]+d[0], p[1]+d[1]]

            # out of bounds
            if np[0] < 0 or np[0] >= self.n or np[1] < 0 or np[1] >= self.m:
                continue

            # goal
            if self.cs[np[0]][np[1]] == 'g':
                self.goal = True
                return

            # not a way
            if self.cs[np[0]][np[1]] == '#' or self.cs[np[0]][np[1]] == 's':
                continue

            # prohibited way
            tnn = int(self.cs[np[0]][np[1]])
            if tnn < n:
                continue

            tn = self.cs[p[0]][p[1]]
            self.cs[p[0]][p[1]] = '#'
            self.move(np, t+1, tnn)
            self.cs[p[0]][p[1]] = tn

        if not self.goal:
            self.move(p, t, n-1)


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    ipt = input().split(' ')
    n = int(ipt[0])
    m = int(ipt[1])
    cs = []
    for i in range(n):
        cs.append(list(input()))

    dwh = DarkWayHome(n, m, cs)
    print(dwh.light)
