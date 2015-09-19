#!/usr/bin/env python


class UpsideDownSort:

    def __init__(self, n, dic):
        self.n = n
        self.dic = dic
        self.sort(0, n-1)

    def sort(self, l, r):
        if l < r:
            i, j = l, r
            pv = self.med3(self.dic[i], self.dic[j], self.dic[i+(j-i)//2])
            while 1:
                while(self.compare(self.dic[i], pv)):
                    i += 1
                while(self.compare(pv, self.dic[j])):
                    j -= 1
                if i >= j:
                    break
                self.dic[i], self.dic[j] = self.dic[j], self.dic[i]
                i += 1
                j -= 1

            self.sort(l, i-1)
            self.sort(j+1, r)

    def med3(self, a, b, c):
        if self.compare(a, b):
            if self.compare(c, b):
                return b
            elif self.compare(c, a):
                return a
            else:
                return c
        else:
            if self.compare(b, c):
                return b
            elif self.compare(a, c):
                return a
            else:
                return c

    def compare(self, a, b):
        m = min(len(a), len(b))
        p = -1
        while p > -m and a[p] == b[p]:
            p -= 1

        if p == -m and a[p] == b[p]:
            return len(a) < len(b)

        return a[p] < b[p]


if __name__ == '__main__':
    n = int(input())
    dic = []
    for i in range(n):
        dic.append(input())
    uds = UpsideDownSort(n, dic)

    for w in uds.dic:
        print(w)
