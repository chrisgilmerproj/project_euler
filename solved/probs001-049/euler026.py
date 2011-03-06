# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #026
#
# Problem:  Find the value of d < 1000 for which 1/d contains the longest
#           recurring cycle in its decimal fraction part.
#
# Hint:     A unit fraction contains 1 in the numerator. The decimal
#           representation of the unit fractions with denominators 2 to 10 are
#           given:
#
#               1/2	= 	0.5
#               1/3	= 	0.(3)
#               1/4	= 	0.25
#               1/5	= 	0.2
#               1/6	= 	0.1(6)
#               1/7	= 	0.(142857)
#               1/8	= 	0.125
#               1/9	= 	0.(1)
#               1/10	= 	0.1
#
#           Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
#           It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Written by Chris Gilmer
# Solved:   12/11/2008
# Answer:   983
#
# Notes:

from decimal import *

def repeat(n):
    if decimal[n:n*2] == decimal[0:n]:
        return True
    else:
        return False


if __name__ == '__main__':
    
    getcontext().prec = 2000
    D = Decimal

    longest = 1
    d_value = 0
    
    for d in range(2,1000):
        fraction = str(D("1.0")/D(d))
        decimal = list(fraction.split('.')[1])
        length = 0
        if len(decimal) >= 6:
            for i in range(5,1000):
                if repeat(i):
                    length = i
                    break

        if length >= longest:
            longest = length
            d_value = d
            print '\n1/%s repeats %s numbers, 0.(%s)' % (d,length,''.join(decimal[0:length]))
            
                
    print '\n\tThe value d = %s has a decimal repeat of length %s numbers\n' % (d_value,longest)
