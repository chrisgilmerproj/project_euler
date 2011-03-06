# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #216
#
# Problem:  How many numbers t(n) are prime for n <= 50,000,000 ?
#
# Hint:     Consider numbers t(n) of the form t(n) = 2n^(2)-1 with n > 1.
#           The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
#           It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
#           For n <= 10000 there are 2202 numbers t(n) that are prime.
#
# Written by Chris Gilmer
# Solved:   
# Answer:   
#
# Notes:

from factor import *

if __name__ == '__main__':

    count = 0
    limit = 10000

    for n in range(2,limit+1):
        t = 2*(n*n)-1
        if isPrime(t):
            count += 1

    print '\n\tFor n <= %s there are %s primes\n' % (limit,count)
