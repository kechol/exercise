#!/usr/bin/env python

import math


class RacingGame:

    def __init__(self):
        self.n = int(input())
        ipt = input().split(' ')

        self.start = [int(ipt[0]), 0]
        self.goal = [int(ipt[1]), self.n]
        self.result = 0.0

        self.p = self.start

        for i in range(self.n):
            ipt = input().split(' ')
            self.turn([int(ipt[0]), i], [int(ipt[1]), i])

        self.result += self.hypot(self.p, self.goal)

        print(self.result)

    def turn(self, l, r):
        d = (self.goal[0] - self.p[0]) / (self.goal[1] - self.p[1])

        if d * (l[1] - self.p[1]) < l[0] - self.p[0]:
            self.result += self.hypot(self.p, l)
            self.p = l

        if d * (r[1] - self.p[1]) > r[0] - self.p[0]:
            self.result += self.hypot(self.p, r)
            self.p = r

    def hypot(self, p0, p1):
        s0 = p0[0] - p1[0]
        s1 = p0[1] - p1[1]
        return math.hypot(s0, s1)


RacingGame()
