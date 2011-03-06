# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #040
#
# Problem:  If dn represents the nth digit of the fractional part, find the value 
#           of the following expression.
#
#           d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
#
# Hint:     An irrational decimal fraction is created by concatenating the positive 
#           integers:
#
#           0.123456789101112131415161718192021...
#
#           It can be seen that the 12th digit of the fractional part is 1.
#
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   210
#
# Notes:

if __name__ == '__main__':

    power = 6
    upper = 10**power
    frac = []
    for i in range(1,upper+1):
        frac.extend(list(str(i)))

    dtotal = 1
    for j in range(power+1):
        print 10**j, frac[10**j-1]
        dtotal *= int(frac[10**j-1])

    print '\n\tThe value of the expression is: %s\n' % dtotal
