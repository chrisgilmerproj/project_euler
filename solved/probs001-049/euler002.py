# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #002
#
# Problem: Find the sum of all the even-valued terms in the
#          sequence which do not exceed four million.
#
# Hint: Each new term in the Fibonacci sequence is generated
#       by adding the previous two terms. By starting with
#       1 and 2, the first 10 terms will be:
#       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# Written by Chris Gilmer
# Solved: 10/14/2008
# Answer: 4613732
#
# Notes: The Fibonacci sequence should start with 0 and 1

x, y = 0, 1
total = 0

while x <= 4000000:
    x, y = y, x+y
    if x%2 == 0:
        total += x

print 'The sum of all the even-valued terms in the sequence which do not exceed four million: %s' % total

