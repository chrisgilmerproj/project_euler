# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #204
#
# Problem:  How many generalised Hamming numbers of type 100 are there
#           which don't exceed 10^9?
#
# Hint:     A Hamming number is a positive number which has no prime factor
#           larger than 5.  So the first few Hamming numbers are
#           1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
#
#           There are 1105 Hamming numbers not exceeding 10^8.
#
#           We will call a positive number a generalised Hamming number of
#           type n, if it has no prime factor larger than n. Hence the Hamming
#           numbers are the generalised Hamming numbers of type 5.
#
# Written by Chris Gilmer
# Solved:   
# Answer:   
#
# Notes:

from factor import *
from math import *
from time import *

def hform(prime_list, exp_list, lim, bound, count, hcount):
    for element in range(exp_list[count-1]+1):
        lim[count-1] = element              # List to carry exponents
        num = 1
        for x in range(len(prime_list)):    # Determine size of number
            num = num*(prime_list[x]**lim[x])
            if num > bound: break
        if count != len(prime_list):        # Only add to hcount at end of list
            count += 1
            hcount = hform(prime_list, exp_list, lim, bound, count, hcount)
            count -= 1  
        elif num > bound: break             # Need to break loop if number too large
        else:
            hcount += 1                     # Continue to count the Hamming numbers
            if hcount % 10000 == 0: print hcount, lim, clock()
    return hcount                           # Return the last calculated Hamming Number

def hamming(smooth,power):

    bound = 10**power

    prime_list = []                         # Generate the prime numbers
    for i in range(smooth+1):
        if isPrime(i):
            prime_list.append(i)
            
    prime_list.reverse()                    # Speeds up calculation

    exp_list = []                           # Determine the maximum exponents can be
    for prime in prime_list:
        exp_list.append(int(log(bound)/log(prime)))

    hcount, count = 0, 1
    lim = [0]*len(prime_list)               # List to carry exponents
    final = hform(prime_list, exp_list, lim, bound, count, hcount)
    
    print '\nThere are %s Hamming numbers of type %s not exceeding 10^%s' % (final, smooth, power)
    print '\tFound in %s seconds' % clock()
    print '\tThere are %s Primes that include: %s' % (len(prime_list),prime_list)
    print '\tThe calculated Exponent limits: %s\n' % exp_list

if __name__ == '__main__':

    hamming(5,8) # 1105, 0.01s
    hamming(100,9)

##    smooth = 17
##    power = 9
##    
##    prime_list = []                         # Generate the prime numbers
##    for i in range(smooth+1):
##        if isPrime(i):
##            prime_list.append(i)
##
##    for x in prime_list:
##        hamming(x,power)


#10000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 5, 0] 0.24
#20000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 1, 0, 0, 5] 0.95
#30000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 6, 0, 2] 4.78
#40000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 0, 5] 6.36
#50000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 1, 2, 0, 0] 18.42
#60000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 4, 3] 35.8
#70000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 2, 2, 0, 3] 44.0
#80000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 2, 3, 0, 0] 74.54
#90000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 4, 2, 2, 1] 271.84
#100000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 2, 1, 1] 276.26
#110000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 2, 0, 7] 306.7
#120000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 1, 7] 535.45
#130000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 0] 795.61
#140000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 3, 3, 5] 1822.4
#150000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 1, 3, 0, 0, 1] 1827.41
#160000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 1, 2, 6] 1865.15
#170000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 3] 2089.33
#180000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1, 1, 0, 0] -672.687296
#190000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 1, 1, 0, 0, 0] -149.177296
#200000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 3, 0, 13] -410.981888
#210000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 3, 0, 2, 0, 0, 0] -405.551888
#220000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 0, 3] -367.541888
#230000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 1, 2, 1, 0] -140.441888
#240000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 3, 1, 3, 0] 1389.598112
#250000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 3, 0, 0]
#260000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 1, 10]
#270000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 1, 1, 0, 0, 0, 3] 1392.744336
#280000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2] 1159.70408
#290000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 4, 1, 2] 1194.32408
#300000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 3, 0, 2, 4] 1428.95408
#310000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 1, 0, 3, 0] 1696.87408
#320000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 1] -1024.663216
#330000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 2, 1, 1, 6] 846.602192
#340000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1] 430.880304
#350000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2] -861.03184
#360000 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0] -186.170464
