# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #028
#
# Problem:  What is the sum of both diagonals in a 1001 by 1001 spiral formed
#           in the same way?
#
# Hint:     Starting with the number 1 and moving to the right in a clockwise
#           direction a 5 by 5 spiral is formed as follows:
#
#           21 22 23 24 25
#           20  7  8  9 10
#           19  6  1  2 11
#           18  5  4  3 12
#           17 16 15 14 13
#
#           It can be verified that the sum of both diagonals is 101.
#
# Written by Chris Gilmer
# Solved:   10/28/2008
# Answer:   669171001
#
# Notes:

def spiral(size):
    spiral = []

    for i in range(size):
        spiral.append([0]*size)

    x = size-1
    y = 0
    
    i = size*size

    xupper = size-1
    yupper = size-1
    xlower = 0
    ylower = 0


    while i >= 1:
        if spiral[y][x] == 0:
            spiral[y][x] = i

        if y == ylower and x > xlower:
                x -= 1
                if x == xlower:
                    ylower += 1
        elif x == xlower and y < yupper:
                y += 1
                if y == yupper:
                    xlower += 1
        elif y == yupper and x < xupper:
                x += 1
                if x == xupper:
                    yupper -= 1
        elif x == xupper and y > ylower:
                y -= 1
                if y == ylower:
                    xupper -= 1
        i -= 1

    return spiral

if __name__ == '__main__':

    size = 1001
    matrix = spiral(size)
    #print matrix
    
    total1, total2 = 0, 0
    x, y = 0, 0

    while x < size:
	#print x,y
        total1 += matrix[x][y]
        x += 1
        y += 1

    x, y = 0, size-1

    while x < size:
        #print x, y
        total2 += matrix[x][y]
        x += 1
	y -= 1

    cross_total = total1 + total2 - 1
	
    print '\n\tThe sum of both diagonals of a %s by %s sprial matrix is:' % (size,size)
    print '\t\t%s + %s - 1 = %s\n' % (total1, total2, cross_total)
