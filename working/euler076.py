# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #076
#
# Problem:  How many different ways can one hundred be written as a sum of at
#           least two positive integers?
#
# Hint:     It is possible to write five as a sum in exactly six different ways:
#
#           4 + 1
#           3 + 2
#           3 + 1 + 1
#           2 + 2 + 1
#           2 + 1 + 1 + 1
#           1 + 1 + 1 + 1 + 1
#
# Written by Chris Gilmer
# Solved:   
# Answer:   
#
# Notes:    You can use more than two positive integers to add to one hundred

def sum_integers(limit):
    count = 0
    
    n = 1
    while n < limit:
        total = 0
        while total < limit:
            i = limit - total

            

            total += n
        n +=1

    return count

if __name__ == '__main__':

    limit = 5
    count = sum_integers(limit)
    
    print '\nThe number %s can be written as the sum of at least two positive integers %s different ways\n' % (limit,count)

#9+1
#8+2
#8+1+1
#7+3
#7+2+1
#7+1+1+1
#6+4
#6+3+1
#6+2+2
#6+2+1+1
#6+1+1+1+1
#5+5
#5+4+1
#5+3+2
#5+3+1+1
#5+2+2+1
#5+2+1+1+1
#5+1+1+1+1+1
#4+4+2
#4+4+1+1
#4+3+3
#4+3+2+1
#4+3+1+1+1
#4+2+2+2
#4+2+2+1+1
#4+2+1+1+1+1
#4+1+1+1+1+1+1
#3+3+3+1
#3+3+2+2
#3+3+2+1+1
#3+3+1+1+1+1
#3+2+2+2+1
#3+2+2+1+1+1
#3+2+1+1+1+1+1
#3+1+1+1+1+1+1+1
#2+2+2+2+2
#2+2+2+2+1+1
#2+2+2+1+1+1+1
#2+2+1+1+1+1+1+1
#2+1+1+1+1+1+1+1+1
#1+1+1+1+1+1+1+1+1+1
