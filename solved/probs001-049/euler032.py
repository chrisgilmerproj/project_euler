# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #032
#
# Problem:  Find the sum of all products whose multiplicand/multiplier/product 
#           identity can be written as a 1 through 9 pandigital.
#
# Hint:     The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing 
#           multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#           HINT: Some products can be obtained in more than one way so be sure to 
#                 only include it once in your sum.
#
# Written by Chris Gilmer
# Solved:   10/29/2008
# Answer:   45228
#
# Notes:

from factor import isPandigital

if __name__ == '__main__':

    num = 0
    products = []
    for i in range(1,1000):
        for j in range(1,10000):
            
            num = i*j
            
            numcheck = int(''.join(list(str(i))+list(str(j))+list(str(num))))
            if isPandigital(numcheck):
	        if not products.__contains__(num):
                    products.append(num)
                print '%s x %s = %s is Pandigital' % (i, j, num)

    print '\n\tThe total of the unique Pandigital products is: %s\n' % sum(products)

