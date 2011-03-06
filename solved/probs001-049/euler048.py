# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #048
#
# Problem:  Find the last ten digits of the series,
#           1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
# Hint:     The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Written by Chris Gilmer
# Solved:   10/21/2008
# Answer:   9110846700
#
# Notes:

if __name__ == '__main__':

    total = 0
    upper = 1000
    for i in range(1,upper+1):
        total += pow(i,i)

    print total
    print list(str(total))[-10:]
