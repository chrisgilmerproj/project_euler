# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #069
#
# Problem:  Find the value of n <= 1,000,000 for which n/phi(n) is a maximum
#
# Hint:     Euler's Totient function, phi(n) [sometimes called the phi function],
#           is used to determine the number of numbers less than n which are
#           relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
#           all less than nine and relatively prime to nine, phi(9)=6.
#
#           n 	Relatively Prime 	phi(n) 	n/phi(n)
#           2 	1 	                1 	2
#           3 	1,2 	                2 	1.5
#           4 	1,3 	                2 	2
#           5 	1,2,3,4 	        4 	1.25
#           6 	1,5 	                2 	3
#           7 	1,2,3,4,5,6 	        6 	1.1666...
#           8 	1,3,5,7 	        4 	2
#           9 	1,2,4,5,7,8 	        6 	1.5
#           10 	1,3,7,9 	        4 	2.5
#
#           It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.
#
# Written by Chris Gilmer
# Solved:   12/16/2008
# Answer:   510510
#
# Notes:    These are numbers where the only common factor between them is 1.
#           Turns out there are commonalities between the growth of numbers,
#           in that each set expands upwards by the common prime factors listed
#           here: 2, 3, 5, 7, 11, 13, 17 (meaning the largest ratio will be
#           produced by multiplying them all together).

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def phi(n):
    p = [1]
    for i in range(2.0,n):
        if gcd(i,n) == 1.0:
            p.append(i)
    return len(p)

if __name__ == '__main__':

    max_p = 0.0
    max_n = 0.0
    n = 1.0

    while n <= 1000000.0:
        if n%2310 == 0:
            p = n / phi(n)
            if p >= max_p:
                max_n = n
                max_p = p
                print n, p, '\t', n/2, n/6, n/30, n/210, n/2310, n/30030, n/510510 # 2, 3, 5, 7, 11, 13, 17

        n += 1.0

    print "n = %s produces a maximum %s" % (max_n,max_p)
