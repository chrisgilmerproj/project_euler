# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #020
#
# Problem:  Find the sum of the digits in the number 100!
#
# Hint:     n! means n x (n  1) x ... x 3 x 2 x 1
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   648
#
# Notes:

if __name__ == '__main__':

    factorial = 1
    total = 0
    for i in range(1,101):
        factorial *= i

    for i in list(str(factorial)):
        total += int(i)

    print total
