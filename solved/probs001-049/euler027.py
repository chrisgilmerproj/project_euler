# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #027
#
# Problem:  Considering quadratics of the form:
#
#           n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#           where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |4| = 4)
#
#           Find the product of the coefficients, a and b, for the quadratic expression that produces
#           the maximum number of primes for consecutive values of n, starting with n = 0.
#
# Hint:     Euler published the remarkable quadratic formula:
#
#           n^2 + n + 41
#
#           It turns out that the formula will produce 40 primes for the consecutive values 
#           n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
#           by 41, and certainly when n = 41, 41? + 41 + 41 is clearly divisible by 41.
#
#           Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 
#           80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 
#           and 1601, is 126479.
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   -59231  is the product of a and b, with 71 consecutive primes for the equation "n^2 + (-61*n) + (971)"
#           -126479 is the product of a and b, with 80 consecutive primes for the equation "n^2 + (-79*n) + (1601)"
#
# Notes:

from factor import *

if __name__ == '__main__':

    a_max, b_max = 1000, 1000
    a_prime, b_prime = 0,0
    longest_prime = 0
    for a in range(-a_max,a_max):
        for b in range(-b_max,b_max):
	    prime_count = 0
	    for n in range(100):
                num = n**2+a*n+b
                if num <= 1:
                    break
	        elif isPrime(num):
		    prime_count += 1
		else: break
	    if prime_count > longest_prime:
	        a_prime = a
		b_prime = b
		longest_prime = prime_count

    print '\n\t%s is the product of a and b, with %s consecutive primes for the equation "n^2 + (%s*n) + (%s)"\n' % (a_prime*b_prime, longest_prime, a_prime, b_prime)
	        
