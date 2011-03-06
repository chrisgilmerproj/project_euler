# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #013
#
# Problem:  Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#
# Hint:     Text file in euler013.txt
#
# Written by Chris Gilmer
# Solved:   10/16/2008
# Answer:   5537376230
#
# Notes:
 
if __name__ == '__main__':

    file = open('euler013.txt', 'r')
    print str(sum([int(line) for line in file]))[:10]
    file.close()
