# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #037
#
# Problem:  Find the sum of the only eleven primes that are both truncatable 
#           from left to right and right to left.
#
# Hint:     The number 3797 has an interesting property. Being prime itself, 
#           it is possible to continuously remove digits from left to right, 
#           and remain prime at each stage: 3797, 797, 97, and 7. Similarly we 
#           can work from right to left: 3797, 379, 37, and 3.
#
#           NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   748317
#
# Notes:

from factor import *

if __name__ == '__main__':

    upper = 10**6
    trun_primes = []
    for i in range(10,upper+1):
        if isPrime(i):
	    trun_word = list(str(i))
	    right_count = 0
	    left_count = 0
	    j = len(trun_word)
	    while j > 0:
	        if isPrime(int(''.join(trun_word[-j:]))):
		    left_count += 1
		else: break
		if isPrime(int(''.join(trun_word[:j]))):
		    right_count += 1
		else: break
		j -= 1
	    
	    if left_count == len(trun_word) and right_count == len(trun_word):
	        trun_primes.append(i)
		print i

    trun_sum = 0
    for element in trun_primes:
        trun_sum += int(element)

    print 'The sum of all eleven truncatable primes equals: %s' % trun_sum
	    
    
