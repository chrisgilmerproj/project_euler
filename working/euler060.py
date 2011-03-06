# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #060
#
# Problem:  Find the lowest sum for a set of five primes for which any two
#           primes concatenate to produce another prime.
#
# Hint:     The primes 3, 7, 109, and 673, are quite remarkable. By taking any
#           two primes and concatenating them in any order the result will
#           always be prime. For example, taking 7 and 109, both 7109 and 1097
#           are prime. The sum of these four primes, 792, represents the lowest
#           sum for a set of four primes with this property.
#
# Written by Chris Gilmer
# Solved:   
# Answer:   
#
# Notes:

from factor import *

def reduce_primes(prime_list):

    new_prime_list = []
    
    for prime in prime_list:
        prime_word = list(str(prime))
        prime_len = len(prime_word)
        for i in range(1,prime_len):
            prime_1 = int(''.join(prime_word[0:i]))
            prime_2 = int(''.join(prime_word[i:prime_len]))

            if isPrime(prime_1) and isPrime(prime_2):
                if not new_prime_list.__contains__(prime_1):
                    new_prime_list.append(prime_1)
                if not new_prime_list.__contains__(prime_2):
                    new_prime_list.append(prime_2)

    return new_prime_list

def final_primes(prime_list):
    final_prime_list = []

    for i in range(0,prime_length):
        count = 0
	for j in range(i,prime_length):
            print i, j
	    prime_1 = int(str(prime_list[i])+str(prime_list[j]))
            prime_2 = int(str(prime_list[j])+str(prime_list[i]))
	    if isPrime(prime_1) and isPrime(prime_2):
	        count += 1
	        
            if count >= 5:
                final_prime_list.append(prime_list[i])
                break
	    
    return final_prime_list

if __name__ == '__main__':

    limit = 1000000

    prime_list = []

    for n in range(2,limit):
        if isPrime(n): prime_list.append(n)

    prime_length = len(prime_list)

    print '\nNumber of primes: ', prime_length

    new_prime_list = reduce_primes(prime_list)
    prime_length = len(new_prime_list)
    prime_list = new_prime_list
    prime_list.sort()
    
    print '\nNumber of leftover primes: ', prime_length

    while prime_length > 5:
        new_prime_list = final_primes(prime_list)
        prime_length = len(new_prime_list)
        prime_list = new_prime_list
        prime_list.sort()
        print '\n', prime_length, prime_list


