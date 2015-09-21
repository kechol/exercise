#!/usr/bin/env python


class DarkWayHome:

    def __init__(self, n, m, cs):
        self.n = n
        self.m = m
        self.cs = cs
        self.light = 0.0
        self.p = [0, 0]

        self.p = self.start_point()
        self.move(0)

    def start_point(self):
        for i in range(self.n):
            if 's' in self.cs[i]:
                return [i, self.cs[i].index('s')]

    def move(self, t):
        print("\n".join(["".join(c) for c in self.cs]), "\n")

        ds = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        l = 0.0
        np = [0, 0]

        for d in ds:
            tnp = [self.p[0]+d[0], self.p[1]+d[1]]

            if tnp[0] < 0 or tnp[0] >= n or tnp[1] < 0 or tnp[1] >= m:
                continue

            if self.cs[tnp[0]][tnp[1]] == '#' or self.cs[tnp[0]][tnp[1]] == 's':
                continue

            if self.cs[tnp[0]][tnp[1]] == 'g':
                return

            tl = float(self.cs[tnp[0]][tnp[1]]) * (0.99 ** t)
            if l < tl:
                l = tl
                np = tnp

        self.cs[np[0]][np[1]] = '#'
        self.light = l
        self.p = np
        self.move(t+1)


if __name__ == '__main__':
    ipt = input().split(' ')
    n = int(ipt[0])
    m = int(ipt[1])
    cs = []
    for i in range(n):
        cs.append(list(input()))

    dwh = DarkWayHome(n, m, cs)
    print(dwh.light)