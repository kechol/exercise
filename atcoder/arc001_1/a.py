#!/usr/bin/env python


class Grading:

    def __init__(self, n, cs):
        self.n = n
        self.cs = cs
        self.cnt = [0]*4

        for c in self.cs:
            self.cnt[int(c)-1] += 1


if __name__ == '__main__':
    n = input()
    cs = input()
    g = Grading(n, cs)
    print("{} {}".format(max(g.cnt), min(g.cnt)))
