# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #019
#
# Problem:  How many Sundays fell on the first of the month during
#           the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Hint:     You are given the following information, but you may prefer to do some research for yourself.
#
#           - 1 Jan 1900 was a Monday.
#           - Thirty days has September,
#               April, June and November.
#               All the rest have thirty-one,
#               Saving February alone,
#               Which has twenty-eight, rain or shine,
#               And on leap years, twenty-nine.
#           - A leap year occurs on any year evenly divisible by 4,
#               but not on a century unless it is divisible by 400.
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   171
#
# Notes:

import datetime, calendar

if __name__ == '__main__':

    datecount = datetime.date(2000, 12, 31)
    oneday = datetime.timedelta(days=1)
    count = 0

    while datecount >= datetime.date(1901, 01, 01):
        if datecount.weekday() == calendar.SUNDAY and datecount.day == 1:
            count += 1
            print datecount.strftime('%A, %d-%b-%Y')
        datecount -= oneday

    print '%s Sundays fell on the first of the month in the 20th century' % count


    
        
        
