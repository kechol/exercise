#!/usr/bin/env python

import sys


class MaxMinDistance:

    def __init__(self, n, ds):
        self.n = n
        self.ds = ds
        self.ds.sort()

    def get_max_length(self):
        mx = 0
        for d in ds:
            mx += d
        return mx

    def get_min_length(self):
        mxd = self.get_max_length() - self.ds[self.n-1] * 2
        if mxd < 0:
            return -mxd
        else:
            return 0


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    n = int(input())
    ds = []
    for i in range(n):
        ds.append(int(input()))

    mmd = MaxMinDistance(n, ds)
    print(mmd.get_max_length())
    print(mmd.get_min_length())
