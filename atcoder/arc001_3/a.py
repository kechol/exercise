#!/usr/bin/env python


class TwistedQs:

    def __init__(self):
        self.map = [['.' for i in range(8)] for j in range(8)]

        # init first Qs
        for i in range(8):
            ipt = input()
            for j in range(8):
                if ipt[j] == 'Q':
                    if self.search(i, j):
                        self.map[i][ipt.index('Q')] = 'Q'
                    else:
                        print('No Answer')
                        exit()

        if self.setQ(0):
            print("\n".join(["".join(cx) for cx in self.map]))
        else:
            print('No Answer')

    def setQ(self, i):
        if i > 7:
            return True

        if 'Q' in self.map[i]:
            return self.setQ(i+1)

        for j in range(8):
            if self.search(i, j):
                self.map[i][j] = 'Q'
                if self.setQ(i+1):
                    return True
                self.map[i][j] = '.'

        return False

    def search(self, y, x):
        for i in range(8):
            if self.map[i][x] == 'Q':
                return False

            if self.map[y][i] == 'Q':
                return False

            p = x + y - i
            if p > -1 and p < 8 and self.map[i][p] == 'Q':
                return False

            p = y - x + i
            if p > -1 and p < 8 and self.map[p][i] == 'Q':
                return False

        return True


TwistedQs()
