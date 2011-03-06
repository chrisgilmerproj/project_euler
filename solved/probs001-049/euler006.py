# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #006
#
# Problem:  Find the difference between the sum of the squares of the
#           first one hundred natural numbers and the square of the sum.
#
# Hint:     The sum of the squares of the first ten natural numbers is,
#           1^2 + 2^2 + ... + 10^2 = 385
#
#           The square of the sum of the first ten natural numbers is,
#           (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
#           Hence the difference between the sum of the squares of the
#           first ten natural numbers and the square of the sum is
#           3025-385 = 2640.
#
# Written by Chris Gilmer
# Solved: 10/15/2008
# Answer:   10   : 2640
#           100  : 25164150
#           1000 : 250166416500
#
# Notes: I learned the reduce() function in Euler #005

def sumofsquares(a, b):
    return a+b*b

def add(a, b):
    return a+b

if __name__ == '__main__':
    num = 100
    sqsum = reduce(add,range(1,num+1))**2
    sumsq = reduce(sumofsquares,range(1,num+1))

    print '\n\tThe difference between the sum of the squares and the square of the sum is: %s' % (sqsum-sumsq)
