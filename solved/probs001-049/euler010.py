# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #010
#
# Problem:  Find the sum of all the primes below two million.
#
# Hint:     The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Written by Chris Gilmer
# Solved:   10/15/2008
# Answer:   142913828922
#
# Notes:

import math

def prime(num):
    if num == 2: return True
    if num < 2 or num%2 == 0: return False
    return not any(num%i == 0 for i in range(3, int(math.sqrt(num))+1,2))

if __name__ == '__main__':
    limit = 2000000
    psum = 0
    for i in range(2,limit+1):
        if prime(i): psum += i
    
    print '\n\tThe sum of all primes below %d is %d\n' % (limit,psum)
