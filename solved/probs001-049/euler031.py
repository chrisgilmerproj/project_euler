# -*- coding: utf-8 -*-
# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #031
#
# Problem:  How many different ways can £2 be made using any number of coins?
#
# Hint:     In England the currency is made up of pound, £, and pence, p, and
#           there are eight coins in general circulation:
#
#           1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
#           It is possible to make £2 in the following way:
#
#           1£1 + 150p + 220p + 15p + 12p + 31p
#
# Written by Chris Gilmer
# Solved:   10/29/2008
# Answer:   73682
#
# Notes:

from factor import *
from math import *
from time import *

def hform(currency_list, value_list, lim, bound, count, hcount):
    for element in range(value_list[count-1]+1):
        lim[count-1] = element              # List to carry exponents
        num = 0 
        for x in range(len(currency_list)):    # Determine size of number
            num += (currency_list[x]*lim[x])
            if num > bound: break
        if count != len(currency_list):        # Only add to hcount at end of list
            count += 1
            hcount = hform(currency_list, value_list, lim, bound, count, hcount)
            count -= 1 
        elif num > bound: break               # Need to break loop if number too large
        elif num == bound:
            hcount += 1                     # Continue to count the Hamming numbers
            if hcount % 1000 == 0: print hcount, lim, clock()
    return hcount                           # Return the last calculated Hamming Number

def currency():

    bound = 200
    
    currency_list = [200,100,50,20,10,5,2,1]
    value_list = [1,2,4,10,20,40,100,200]

    hcount, count = 0, 1
    lim = [0]*len(currency_list)               # List to carry exponents
    final = hform(currency_list, value_list, lim, bound, count, hcount)
    
    print '\nThere are %s combinations of English currency not exceeding %s pence' % (final, bound)
    print '\tFound in %s seconds' % clock()

if __name__ == '__main__':

    currency()
    
