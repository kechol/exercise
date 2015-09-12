#!/usr/bin/env python


class CrazyBot:

    def __init__(self):
        self.map = []
        self.dir = []
        self.prb = []

    def getProbability(self, n, east, west, south, north):
        self.map = [[0 for i in range(n*2+1)] for j in range(n*2+1)]
        self.dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        self.prb = [east/100.0, west/100.0, south/100.0, north/100.0]
        return self.step([n, n], n)

    def step(self, xy, n):
        if(self.map[xy[0]][xy[1]]):
            return 0.0

        if(n == 0):
            return 1.0

        self.map[xy[0]][xy[1]] = 1

        result = 0.0
        for i in range(4):
            d = self.dir[i]
            result += self.step([xy[0] + d[0], xy[1] + d[1]], n - 1) * self.prb[i]

        self.map[xy[0]][xy[1]] = 0

        return result


cb = CrazyBot()
print(cb.getProbability(1, 25, 25, 25, 25))  # 1.0
print(cb.getProbability(2, 25, 25, 25, 25))  # 0.75
print(cb.getProbability(7, 50,  0,  0, 50))  # 1.0
