# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #063
#
# Problem:  How many n-digit positive integers exist which are also an
#           nth power?
#
# Hint:     The 5-digit number, 16807=7^5, is also a fifth power. Similarly,
#           the 9-digit number, 134217728=8^9, is a ninth power.
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   49
#
# Notes:

if __name__ == '__main__':

    upper = 100
    n_list = []

    for power in range(0,upper+1):
        num = 10**(power-1)
        i = 1
        while num < 10**power:
            num = i**power
            if len(list(str(num))) == power:
                print '%s^%s = %s' % (i, power, num)
                n_list.append(num)
            i += 1

    print '\n\tThere are %s n-digit positive integers which are also an nth power\n' % len(n_list)
