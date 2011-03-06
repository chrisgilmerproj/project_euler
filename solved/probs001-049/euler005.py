# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #005
#
# Problem:  What is the smallest number that is evenly divisible
#           by all of the numbers from 1 to 20?
#
# Hint:     2520 is the smallest number that can be divided by each
#           of the numbers from 1 to 10 without any remainder.
#
# Written by Chris Gilmer
# Solved: 10/15/2008
# Answer: 232792560
#
# Notes: I didn't actually solve this one so I had better understand the solution

# Greatest Common Denomenator
# This just looks for the GCD and returns it.
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

# Least Common Multiplier
# Multiplies the last value by the next number in the sequence.
# Then it divides out the largest common denominator, which is
# already in the sequence from 1 to 20.
def lcm(a, b):
    return a*b/gcd(a, b)

if __name__ == '__main__':
    print '\n\tThe smallest number evenly divisible by all the numbers from 1 to 20 is: %s' % reduce(lcm, range(1,20+1))
