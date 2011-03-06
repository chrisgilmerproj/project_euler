# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #038
#
# Problem:  What is the largest 1 to 9 pandigital 9-digit number that can be
#           formed as the concatenated product of an integer with (1,2, ... , n)
#           where n 1?
#
# Hint:     Take the number 192 and multiply it by each of 1, 2, and 3:
#
#           192 x 1 = 192
#           192 x 2 = 384
#           192 x 3 = 576
#
#           By concatenating each product we get the 1 to 9 pandigital,
#           192384576. We will call 192384576 the concatenated product of 192
#           and (1,2,3)
#
#           The same can be achieved by starting with 9 and multiplying by 1, 2,
#           3, 4, and 5, giving the pandigital, 918273645, which is the
#           concatenated product of 9 and (1,2,3,4,5).
#
# Written by Chris Gilmer
# Solved:   10/30/2008
# Answer:   932718654
#
# Notes:

from factor import *

if __name__ == '__main__':

    upper = 10**4
    i = 1

    largest = 0

    while i < upper:
        n = 0
        word = []
        while len(word) < 9:
            n += 1
            num = n*i
            word.extend(list(str(num)))
            #print '%s x %s = %s, %s' % (i, n, num, word)
        if isPandigital(int(''.join(word))):
            for j in range(1,n+1):
                new_num = i*j
                print '\t%s x %s = %s' % (i, j, new_num)
            print '\t%s\n' % word
            if int(''.join(word)) > largest:
                largest = int(''.join(word))
        i += 1

    print '\tThe largest pandigital formed in this way is: %s\n' % largest
    
