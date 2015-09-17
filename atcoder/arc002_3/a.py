#!/usr/bin/env python

import sys


class FightCommand:

    def __init__(self, n, command):
        self.n = n
        self.command = command
        self.shortcuts = ['AA', 'AB', 'AX', 'AY',
                          'BB', 'BA', 'BX', 'BY',
                          'XX', 'XA', 'XB', 'XY',
                          'YY', 'YA', 'YB', 'YX']
        self.min = self.n

    def shortcut(self):
        for li in range(16):
            for ri in range(16):
                if li == ri:
                    continue

                cnt = self.count(0, 0, li, ri)
                if self.min > cnt:
                    self.min = cnt

        return self.min

    def count(self, s, c, l, r):
        if s >= self.n:
            return c

        if self.shortcuts[l] == self.command[s:s+2]:
            return self.count(s+2, c+1, l, r)

        if self.shortcuts[r] == self.command[s:s+2]:
            return self.count(s+2, c+1, l, r)

        return self.count(s+1, c+1, l, r)


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    n = int(input())
    c = input()
    fc = FightCommand(n, c)
    print("{}".format(fc.shortcut()))
