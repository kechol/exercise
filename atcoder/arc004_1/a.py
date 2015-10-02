#!/usr/bin/env python

import sys


class LineLength:

    def __init__(self, n, ps):
        self.n = n
        self.ps = ps

    def get_max_length(self):
        l2 = 0
        for i in range(n):
            p1 = self.ps[i]
            for j in range(i+1, n):
                p2 = self.ps[j]
                tl2 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
                if l2 < tl2:
                    l2 = tl2
        return l2 ** 0.5


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    n = int(input())
    ps = []
    for i in range(n):
        ipt = input().split(' ')
        ps.append((int(ipt[0]), int(ipt[1])))

    ll = LineLength(n, ps)
    print(ll.get_max_length())
