# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #012
#
# Problem:  What is the value of the first triangle number to have over five hundred divisors?
#
# Hint:     
#
# Written by Chris Gilmer
# Solved:   10/15/2008
# Answer:   76576500 with 576 divisors
#
# Notes:

from math import sqrt
    
def triangular(n):
    return n*(n+1)/2
 
def divisors(n):
    divs = []
    for d in xrange(1, int(sqrt(n))+1):
        if n % d == 0:
            divs.append(d)
            divs.append(n/d)
    return divs
 
if __name__ == '__main__':

    div,limit = 0,500
    n,t = 2,1
    while div < limit:
        t = triangular(n)
        n += 1
        if len(divisors(t)) > div:
               div = len(divisors(t))
               print '\tNumber: %s\tSeries: %s\tDivisors: %s' % (t, n-1, div)


##	Number: 3	Series: 2	Divisors: 2
##	Number: 6	Series: 3	Divisors: 4
##	Number: 28	Series: 7	Divisors: 6
##	Number: 36	Series: 8	Divisors: 10
##	Number: 120	Series: 15	Divisors: 16
##	Number: 300	Series: 24	Divisors: 18
##	Number: 528	Series: 32	Divisors: 20
##	Number: 630	Series: 35	Divisors: 24
##	Number: 2016	Series: 63	Divisors: 36
##	Number: 3240	Series: 80	Divisors: 40
##	Number: 5460	Series: 104	Divisors: 48
##	Number: 25200	Series: 224	Divisors: 90
##	Number: 73920	Series: 384	Divisors: 112
##	Number: 157080	Series: 560	Divisors: 128
##	Number: 437580	Series: 935	Divisors: 144
##	Number: 749700	Series: 1224	Divisors: 162
##	Number: 1385280	Series: 1664	Divisors: 168
##	Number: 1493856	Series: 1728	Divisors: 192
##	Number: 2031120	Series: 2015	Divisors: 240
##	Number: 2162160	Series: 2079	Divisors: 320
##	Number: 17907120	Series: 5984	Divisors: 480
##	Number: 76576500	Series: 12375	Divisors: 576
##	Number: 103672800	Series: 14399	Divisors: 648
##	Number: 236215980	Series: 21735	Divisors: 768
##	Number: 842161320	Series: 41040	Divisors: 1024
