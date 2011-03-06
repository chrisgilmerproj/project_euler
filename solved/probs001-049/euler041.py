# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #041
#
# Problem:  What is the largest n-digit pandigital prime that exists?
#
# Hint:     We shall say that an n-digit number is pandigital if it makes use
#           of all the digits 1 to n exactly once. For example, 2143 is a
#           4-digit pandigital and is also prime.
#
# Written by Chris Gilmer
# Solved:   10/29/2008
# Answer:   7652413
#
# Notes:

from factor import *

if __name__ == '__main__':
    
    lpower = 6
    upower = 7
    
    pandigital_prime_list = []
    for i in range(10**lpower,10**upower):
        if isPrime(i) and isPandigital(i):
            pandigital_prime_list.append(i)
            print i
