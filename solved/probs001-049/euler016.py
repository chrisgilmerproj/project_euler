# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #016
#
# Problem:  What is the sum of the digits of the number 2^1000?
#
# Hint:     2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   1366
#
# Notes:


if __name__ == '__main__':

    power = 1000
    num = pow(2,power)
    to_add = list(str(num))
    total = 0
    
    for i in to_add:
        total += int(i)

    print '\n\tThe sum of the digits in the number 2^%s is %s' % (power,total)
    print '\tThe number 2^%s = %s\n' % (power,num)
    
    # print sum(int(i) for i in str(2**1000))
