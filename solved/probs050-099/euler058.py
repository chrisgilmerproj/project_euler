# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #058
#
# Problem:  If one complete new layer is wrapped around the spiral above, a
#           square spiral with side length 9 will be formed. If this process
#           is continued, what is the side length of the square spiral for
#           which the ratio of primes along both diagonals first falls
#           below 10%?
#
# Hint:     Starting with 1 and spiralling anticlockwise in the following way,
#           a square spiral with side length 7 is formed.
#
#           37 36 35 34 33 32 31
#           38 17 16 15 14 13 30
#           39 18  5  4  3 12 29
#           40 19  6  1  2 11 28
#           41 20  7  8  9 10 27
#           42 21 22 23 24 25 26
#           43 44 45 46 47 48 49
#
#           It is interesting to note that the odd squares lie along the bottom
#           right diagonal, but what is more interesting is that 8 out of the
#           13 numbers lying along both diagonals are prime; that is, a ratio
#           of 8/13 ~ 62%.
#
# Written by Chris Gilmer
# Solved:   12/12/2008
# Answer:   26241
#
# Notes:    This program takes too long if you try to build the spiral.  Instead I only built
#           the corners of the spiral and checked if they were primes.  

from factor import *

if __name__ == '__main__':
    
    corner_counter = 1.0
    prime_counter = 0.0

    number = 1
    number_skip = 2
    
    percentage = 1.0

    while percentage > 0.1:

        for i in range(0,4):
            number += number_skip
            corner_counter += 1.0

            if isPrime(number):
                prime_counter += 1.0

        percentage = prime_counter/corner_counter
        print 'For spiral of side length %s you get %s/%s = %s' % ((corner_counter+1)/2,prime_counter, corner_counter, percentage)

        number_skip += 2

    print '\n\tThe first square spiral for which the ratio of primes to numbers on the diagonal axis is of length %s\n' % str((corner_counter+1)/2)
