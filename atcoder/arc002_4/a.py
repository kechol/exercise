#!/usr/bin/env python

import sys


class BoardGame:

    def __init__(self, h, w, b):
        self.h = h
        self.w = w
        self.board = b

    def judge(self):
        while self.move('o', 1):
            if not self.move('x', -1):
                return True

        return False

    def move(self, p, d):
#        print("\n".join(["".join(self.board[i]) for i in range(self.h)]), "\n")

        dist = self.w
        coor = [0, 0]
        movable = False
        for i in range(self.h):
            if self.board[i][0] == 'x' or self.board[i][w-1] == 'o':
                return False

            rng = range(0, self.w+d) if (d < 0) else range(d, self.w)
            for j in rng:
                if self.board[i][j] == p:

                    tdist = j if d < 0 else self.w - j - 1
                    if self.board[i][j+d] == '.' and dist > tdist:
                        if (d > 0 and j+d*2 > self.w - 1) or \
                           (d < 0 and j+d*2 < 0) or \
                           self.board[i][j+d*2] in ['.', p]:
                            movable = True
                            coor = [i, j]
                            dist = tdist

        if movable:
            self.board[coor[0]][coor[1]] = '.'
            self.board[coor[0]][coor[1]+d] = p

        return movable


if __name__ == '__main__':
    sys.setrecursionlimit(int(10e8))
    ipt = input().split(' ')
    h = int(ipt[0])
    w = int(ipt[1])
    b = []
    for i in range(h):
        b.append(list(input()))

    bg = BoardGame(h, w, b)
    if bg.judge():
        print('o')
    else:
        print('x')
