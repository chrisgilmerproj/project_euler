# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #
#
# Problem:  Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
#           and 6x, contain the same digits.
#
# Hint:     It can be seen that the number, 125874, and its double, 251748,
#           contain exactly the same digits, but in a different order.
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   142857
#
# Notes:

if __name__ == '__main__':

    num = 0
    contains = False

    while contains == False:
        num += 1
        numstr = list(str(num)) # number we check against
        numstr.sort()

        numtwo = list(str(num*2))
        numtwo.sort()
        if numtwo == numstr:
            numthree = list(str(num*3))
            numthree.sort()
            if numthree == numstr:
                numfour = list(str(num*4))
                numfour.sort()
                if numfour == numstr:
                    numfive = list(str(num*5))
                    numfive.sort()
                    if numfive == numstr:
                        numsix = list(str(num*6))
                        numsix.sort()
                        if numsix == numstr:
                            contains = True

    print num
