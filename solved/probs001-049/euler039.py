# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #039
#
# Problem:  For which value of p < 1000, is the number of solutions maximised?
#
# Hint:     If p is the perimeter of a right angle triangle with integral
#           length sides, {a,b,c}, there are exactly three solutions for
#           p = 120.
#
#           {20,48,52}, {24,45,51}, {30,40,50}
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   840
#
# Notes:

from math import *

if __name__ == '__main__':

    greatest_p, last_count = 0,0

    for p in range(1,1000):
        count = 0
        for a in range(1,500):
            for b in range(1,500):
                c = sqrt(a**2 + b**2)
                num = a + b + c
                if num == p and c%1 == 0:
                    count += 1
                    #print p, a, b, c
        if count > last_count:
            last_count = count
            greatest_p = p
            print p, count
                
    print greatest_p, last_count
