# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #001
#
# Problem: Find the sum of all the multiples of 3 or 5 below 1000.
#
# Hint: If we list all the natural numbers below 10 that are
#       multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
#       these multiples is 23.
#
# Written by Chris Gilmer
# Solved: 10/14/2008
# Answer: 233168
#
# Notes: The real conceptual problem I had with this program
#        was that some multiples of 3 and 5 are the same
#        and I continued to count them twice.

# Original Solution:

##three, five, fifteen = 0, 0, 0
##i, j, k = 1, 1, 1
##
##while 3*i < 1000:
##    three += 3*i
##    i += 1
##
##while 5*j < 1000:
##    five += 5*j
##    j += 1
##
##while 15*k < 1000:
##    fifteen += 15*k
##    k += 1
##
##total = three+five-fifteen

# A more elegant solution:

total = 0

for x in range(1000):
    if (x%3==0) or (x%5==0):
        total += x

print "\nThe sum of all the multiples of 3 or 5 below 1000: %s\n" % (total)



