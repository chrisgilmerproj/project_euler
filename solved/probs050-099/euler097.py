# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #097
#
# Problem:  Find the last ten digits of this prime number: 28433 x 2^7830457+1
#
# Hint:     The first known prime found to exceed one million digits was discovered 
#           in 1999, and is a Mersenne prime of the form 269725931; it contains exactly 
#           2,098,960 digits. Subsequently other Mersenne primes, of the form 2p1, have 
#           been found which contain more digits.
#
#           However, in 2004 there was found a massive non-Mersenne prime which contains 
#           2,357,207 digits: 28433 x 2^7830457+1.
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   8739992577
#
# Notes:

if __name__ == '__main__':

    power = 7830457
    total = 1
    length = 1
    for i in range(1,power + 1):
        total *= 2
	num = list(str(total))
	if len(num) > length and length < 10:
	    length += 1
	#print num[-length:], i
	total = int(''.join(num[-length:]))

    total *= 28433
    total += 1
    total = int(''.join(list(str(total))[-length:]))
    
    print '\n\tThe last ten digits of the prime number "28433 x 2^7830457+1" are %s\n' % total
