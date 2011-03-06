# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #046
#
# Problem:  What is the smallest odd composite that cannot be written as the
#           sum of a prime and twice a square?
#
# Hint:     It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
#           9 = 7 + 2x1^(2)
#           15 = 7 + 2x2^(2)
#           21 = 3 + 2x3^(2)
#           25 = 7 + 2x3^(2)
#           27 = 19 + 2x2^(2)
#           33 = 31 + 2x1^(2)
#
#           It turns out that the conjecture was false.
#
# Written by Chris Gilmer
# Solved:   12/11/2008
# Answer:   5777
#
# Notes:

from factor import *
from math import *

if __name__ == '__main__':

    prime_list = []
    for num in range(1,10000):
        if isPrime(num): prime_list.append(num)

    for i in range(3,10000):
        if not i%2 == 0 and not isPrime(i):
            composite = 0
            while composite != i:
                for prime in prime_list:
                    if prime > i:
                        break
                    else:
                        square_limit = sqrt((i-prime)/2)+1
                        for square in range(0,square_limit):
                            composite = prime + 2*(square**2)
                            if composite == i: break
                    if composite == i: break
            print "%s = %s + 2x%s^2" % (composite, prime, square)
                
            
