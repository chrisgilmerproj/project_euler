# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #049
#
# Problem:  What 12-digit number do you form by concatenating the three terms
#           in this sequence?
#
# Hint:     The arithmetic sequence, 1487, 4817, 8147, in which each of the
#           terms increases by 3330, is unusual in two ways: (i) each of the
#           three terms are prime, and, (ii) each of the 4-digit numbers are
#           permutations of one another.
#
#           There are no arithmetic sequences made up of three 1-, 2-, or
#           3-digit primes, exhibiting this property, but there is one other
#           4-digit increasing sequence.
#
# Written by Chris Gilmer
# Solved:   12/09/2008
# Answer:   2969 6299 9629 with count 3330

#
# Notes:

from factor import *

if __name__ == '__main__':

    i = 1000
    limit = 9999
    primes = []

    while i <= limit:
        if isPrime(i):
            primes.append(i)
        i += 1

    print "\nThe arithmetic sequences with permutable numbers are:"
    for num in primes:
        count = 1000
        while count*2 <= 10000-num:
            num1 = num + count
            num2 = num + count*2
            
            if isPrime(num1) and isPrime(num2):
                perm = list(str(num))
                perm.sort()
                perm1 = list(str(num1))
                perm1.sort()
                perm2 = list(str(num2))
                perm2.sort()
                if perm == perm1 and perm == perm2:
                    print "\t",num, num1, num2, "with count", count
                    
            count += 1
            
