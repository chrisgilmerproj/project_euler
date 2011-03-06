# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #035
#
# Problem:  How many circular primes are there below one million?
#
# Hint:     The number, 197, is called a circular prime because all rotations of
#           the digits: 197, 971, and 719, are themselves prime.
#
#           There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
#           37, 71, 73, 79, and 97.   
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   There are 55 circular primes below 10^6
#
# Notes:    Circular primes actually rotate and are not simply permutations

from factor import *
from time import *

def circulate(seq):
    """circulate a sequence and return a list of the circulations"""
    if not seq:
        return [seq] # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            temp.append(seq[k:] + seq[:k])
            
    return temp

def prime_list(power):
    upper = 10**power
    
    primelist = []
    for i in range(2,upper+1):
        even = True
        if isPrime(i):
	    for item in list(str(i)):
	    	if int(item) % 2 == 0 and i != 2:
		    even = False
		    break
	    if even:
                primelist.append(i)

    print '\n\t%s Odd Permutable Primes to check below 10^%s' % (len(primelist),power)
    return primelist

def circular_prime(power):
    cir_prime = []

    for element in prime_list(power):
        
	circular = True

        for number in circulate(list(str(element))):#prime_permutations:
            if not isPrime(int(''.join(number))):
	        circular = False
	        break
	    
        if circular: cir_prime.append(element)

    print '\t%s Circular Primes found below 10^%s in %s seconds' % (len(cir_prime),power,clock())
    print '\tList:', cir_prime, '\n'

if __name__ == '__main__':

    circular_prime(2) # 13 primes
    #circular_prime(3) # 25 primes
    #circular_prime(4) # 33 primes
    #circular_prime(5) # 43 primes
    circular_prime(6) # 55 primes

    
