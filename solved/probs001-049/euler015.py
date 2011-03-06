# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #015
#
# Problem:  How many routes are there through a 20x20 grid?
#
# Hint:     Starting in the top left corner of a 2x2 grid, there are 6
#           routes (without backtracking) to the bottom right corner.
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   137846528820
#
# Notes:

def get_paths(dimensions):
    seq = [1]
    for i in xrange(dimensions):
        for n in xrange(i):
            seq[n + 1] += seq[n]
        seq.append(seq[-1] * 2)
    return seq[-1]

if __name__ == '__main__':

    # Test it out:
    print 'The number of paths for  2 x 2  grid is: %s' % get_paths(2)
    print 'The number of paths for 20 x 20 grid is: %s' % get_paths(20)
        
    
        
