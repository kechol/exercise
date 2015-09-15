#!/usr/bin/env python


class LeapYear:

    def check(self, year):
        if(year % 4 == 0):
            if(year % 400 == 0 or year % 100 != 0):
                return True

        return False


if __name__ == '__main__':
    i = int(input())
    ly = LeapYear()

    if ly.check(i):
        print('YES')
    else:
        print('NO')
