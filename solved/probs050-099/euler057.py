# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #057
#
# Problem:  In the first one-thousand expansions, how many fractions contain a
#           numerator with more digits than denominator?
#
# Hint:     It is possible to show that the square root of two can be expressed
#           as an infinite continued fraction.
#
#           sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
#           By expanding this for the first four iterations, we get:
#           
#           1 + 1/2 = 3/2 = 1.5
#           1 + 1/(2 + 1/2) = 7/5 = 1.4
#           1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#           1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#           
#           The next three expansions are 99/70, 239/169, and 577/408, but the
#           eighth expansion, 1393/985, is the first example where the number
#           of digits in the numerator exceeds the number of digits in the
#           denominator.
#
# Written by Chris Gilmer
# Solved:   12/11/2008
# Answer:   153
#
# Notes:

def expand(n):
    num, den = 1, 2
    for i in range(1,n):
        num, den = den, num+2*den
    return num, den

def nth(n):
    num,den = expand(n)
    return len(str(num+den)) > len(str(den))

if __name__ == '__main__':

    limit = 1000

    counter = 0
    for n in range(0,limit):
        if nth(n+1): counter +=1

    print "\n%s numerators are larger than the denominators in this expansion\n" % counter
