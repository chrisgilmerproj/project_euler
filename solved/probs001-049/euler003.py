# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #003
#
# Problem: What is the largest prime factor of the number 600851475143 ?
#
# Hint: The prime factors of 13195 are 5, 7, 13 and 29.
#
# Written by Chris Gilmer
# Solved: 10/14/2008
# Answer: 6857
#
# Notes: Each time you find a factor your search area decreases.
#        This means you can dramatically speed up the search time.

def primefactor(num):
    original = num
    limit = num/2+1
    i = 2
    powers = []

    # Find all the factors of a number
    while i <= limit:
        while num%i == 0: # i is factor of num
            powers.append(i)
            num = num/i
        i += 1
        if num == 1: break # all factors found
    
    if len(powers) == 0:
        powers.append(num) # num is prime

    print 'The prime factors of %s: %s\n' % (original,powers)
   
if __name__ == '__main__':
    print '\n'
    primefactor(13195)
    primefactor(600851475143)
