# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #050
#
# Problem:  Which prime, below one-million, can be written as the sum of the
#           most consecutive primes?
#
# Hint:     The prime 41, can be written as the sum of six consecutive primes:
#           41 = 2 + 3 + 5 + 7 + 11 + 13
#
#           This is the longest sum of consecutive primes that adds to a prime
#           below one-hundred.
#
#           The longest sum of consecutive primes below one-thousand that adds
#           to a prime, contains 21 terms, and is equal to 953.
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   997651
#
# Notes:

from factor import *

if __name__ == '__main__':

    upper = 10**6

    prime_list = []
    for i in range(11,upper+1):
        if isPrime(i):
            prime_list.append(i)

    total = 0
    largest_prime = 1

    for element in prime_list:
        total += element
        if total > upper:
            break
        if isPrime(total):
            largest_prime = total
            #print element, total

    print largest_prime

#02 958577
#03 920291
#05 978037
#07 997651
