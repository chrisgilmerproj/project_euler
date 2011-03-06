# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #047
#
# Problem:  Find the first four consecutive integers to have four distinct
#           primes factors. What is the first of these numbers?
#
# Hint:     The first two consecutive numbers to have two distinct prime factors are:
#
#           14 = 2 x 7
#           15 = 3 x 5
#
#           The first three consecutive numbers to have three distinct prime factors are:
#
#           644 = 2^2 x 7 x 23
#           645 = 3 x 5 x 43
#           646 = 2 x 17 x 19.
#
# Written by Chris Gilmer
# Solved:   12/11/2008
# Answer:   134043
#
# Notes:

from factor import *

if __name__ == '__main__':

    distinct_primes = 4

    for i in range(1,1000000):
        if len(prime_factors(i)) == distinct_primes:
            if len(prime_factors(i+1)) == distinct_primes:
                if len(prime_factors(i+2)) == distinct_primes:
                    print i, i+1, i+2
                    if len(prime_factors(i+3)) == distinct_primes:
                        print i, i+1, i+2, i+3
                        break
            
