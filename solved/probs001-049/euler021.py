# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #021
#
# Problem:  Evaluate the sum of all the amicable numbers under 10000.
#
# Hint:     Let d(n) be defined as the sum of proper divisors of n
#           (numbers less than n which divide evenly into n).
#           If d(a) = b and d(b) = a, where a b, then a and b are an
#           amicable pair and each of a and b are called amicable numbers.
#
#           For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
#           20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors
#           of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Written by Chris Gilmer
# Solved:   10/21/2008
# Answer:   31626
#
# Notes:

from factor import * 

if __name__ == '__main__':

    total = 0
    upper = 10000
    for num in range(1,upper+1):
        if num == sum(all_factors(sum(all_factors(num)))) and num != sum(all_factors(num)):
            print num, sum(all_factors(num))
            total += num

    print '\n\t The sum of all unique amicable numbers under %s is %s\n' % (upper,total)
