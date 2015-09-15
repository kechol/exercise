#!/usr/bin/env python


class DivisibleDate:
    # not a leap year
    LAST_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def date(self, y, m, d):
        if(y % (m * d) == 0):
            return "{0:0>4}/{1:0>2}/{2:0>2}".format(y, m, d)

        if(m == 12 and d == DivisibleDate.LAST_DAYS[11]):
            return self.date(y+1, 1, 1)

        if(self.is_leap_year(y) and m == 2 and d == DivisibleDate.LAST_DAYS[1]):
            return self.date(y, m, d+1)

        if(d >= DivisibleDate.LAST_DAYS[m-1]):
            return self.date(y, m+1, 1)
        else:
            return self.date(y, m, d+1)

    def is_leap_year(self, year):
        if(year % 4 == 0):
            if(year % 400 == 0 or year % 100 != 0):
                return True

        return False


if __name__ == '__main__':
    ipt = input().split('/')
    dd = DivisibleDate()
    print(dd.date(int(ipt[0]), int(ipt[1]), int(ipt[2])))
