# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #009
#
# Problem:  Find the product of abc.
#
# Hint:     A Pythagorean triplet is a set of three natural numbers,
#           a < b < c, for which a^2 + b^2 = c^2.
#
#           For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
#           There exists exactly one Pythagorean triplet for which
#           a + b + c = 1000.
#
# Written by Chris Gilmer
# Solved:   10/15/2008
# Answer:   a = 375, b = 200, c = 425
#           product is 31875000
#
# Notes:    


if __name__ == '__main__':
    limit = 1000
    for i in range(1,limit):
        if (500000-1000*i)%(1000-i) == 0:
            b = i
            a = (500000-1000*i)/(1000-i)
            c = 1000 - a - b
            print "\ta = %d, b = %d, c = %d" %(a, b, c)
            print "\tproduct is %d" %(a*b*c)
            break

# Sweet Solution
## from math import sqrt
## limit = 1000
## [a * b * sqrt(a**2 + b**2) for a in range(1, limit/2) for b in range(1, limit/2) if a + b + sqrt(a**2 + b**2) == limit]
