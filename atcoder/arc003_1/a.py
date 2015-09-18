#!/usr/bin/env python


class GPACalc:

    def __init__(self, n, ranks):
        self.n = n
        self.ranks = ranks
        self.gpa = 0
        self.conv = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

        for r in self.ranks:
            self.gpa += self.conv[r]

        self.gpa /= self.n


if __name__ == '__main__':
    n = int(input())
    ranks = list(input())
    gc = GPACalc(n, ranks)
    print(gc.gpa)
