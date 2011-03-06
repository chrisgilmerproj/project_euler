# -*- coding: utf-8 -*-
# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #053
#
# Problem:  How many, not necessarily distinct, values of  ^(n)C_(r),
#           for 1 <= n <= 100, are greater than one-million?
#
# Hint:     There are exactly ten ways of selecting three from five, 12345:
#
#           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#           In combinatorics, we use the notation, ^(5)C_(3) = 10.
#
#           In general,
#
#           ^(n)C_(r) = n!/(r!(n−r)!),
#
#           where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#
#           It is not until n = 23, that a value exceeds one-million:
#           ^(23)C_(10) = 1144066.
#
# Written by Chris Gilmer
# Solved:   12/11/2008
# Answer:   4075
#
# Notes:

def fact(x):
    return (1 if x==0 else x * fact(x-1))

def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))

if __name__ == '__main__':

    n = 1
    n_limit = 100
    count = 0

    for n in range(1,n_limit+1):
        for r in range(1,n):
            if combination(n,r) > 1000000:
                count += 1

    print "\n\t%s combinations are greater than one million\n" % count
