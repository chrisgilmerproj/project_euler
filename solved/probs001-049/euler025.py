# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #019
#
# Problem:  What is the first term in the Fibonacci sequence to contain 1000 digits?
#
# Hint:     
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   4782
#
# Notes:

if __name__ == '__main__':

    x, y = 0, 1
    count = 0
    
    while len(list(str(x))) < 1000:
        x, y = y, x+y
        count += 1

    print count
