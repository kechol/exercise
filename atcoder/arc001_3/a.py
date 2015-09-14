#!/usr/bin/env python


class Queen:

    def __init__(self):
        self.map = [['.' for i in range(8)] for j in range(8)]

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


if __name__ == '__main__':
    q = Queen()

    for i in range(8):
        ipt = input()
        # use for-loop in case more than one Qs in same row
        for j in range(8):
            if ipt[j] == 'Q':
                # check if invalid
                if q.search(i, j):
                    q.map[i][j] = 'Q'
                else:
                    print('No Answer')
                    exit()

    if q.setQ(0):
        print("\n".join(["".join(mx) for mx in q.map]))
    else:
        print('No Answer')
