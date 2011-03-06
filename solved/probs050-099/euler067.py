# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #067
#
# Problem:  Find the maximum total from top to bottom in euler067.txt,
#           a 15K text file containing a triangle with one-hundred rows.
#
# Hint:     By starting at the top of the triangle below and moving to
#           adjacent numbers on the row below, the maximum total from top
#           to bottom is 23.
#
#           3
#           7 5
#           2 4 6
#           8 5 9 3
#
#           That is, 3 + 7 + 4 + 9 = 23.
#
#           NOTE: This is a much more difficult version of Problem 18.
#           It is not possible to try every route to solve this problem,
#           as there are 2^99 altogether! If you could check one trillion (10^12)
#           routes every second it would take over twenty billion years to
#           check them all. There is an efficient algorithm to solve it. ;o)
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   7273
#
# Notes:

if __name__ == '__main__':

    file = open('euler067.txt', 'r')
    triangle = []

    # Make a list of lists for the data
    for line in file:
        triangle.append((line.replace('\n','')).split(' '))

    # Convert all the strings to integers
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] = int(triangle[i][j])

    # Flatten the triangle
    for i in range(1,len(triangle)): # Start at second row to avoid addition errors
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][len(triangle[i-1])-1]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
                
    print '\n\tThe maximum total from top to bottom of the given triangle is %s\n' % max(triangle[i])
    
    file.close()
