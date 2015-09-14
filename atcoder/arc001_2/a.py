#!/usr/bin/env python

"""
1=1+
2=1+1+
3=5+1-1-
4=5+1-
5=5+
6=5+1+
7=5+1+1+
8=10+1-1-
9=10+1-
"""


class Remote:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.cnt = 0
        self.calc()

    def calc(self):
        gap = abs(self.b - self.a)
        self.cnt += gap // 10
        gap %= 10

        rem = gap % 5
        if(rem > 2):
            rem = 5 - rem

        self.cnt += rem

        if(gap > 2):
            self.cnt += 1


if __name__ == '__main__':
    ipt = input().split(' ')
    r = Remote(int(ipt[0]), int(ipt[1]))
    print(r.cnt)
