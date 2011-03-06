# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #024
#
# Problem:  What is the millionth lexicographic permutation of the digits
#           0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# Hint:     A permutation is an ordered arrangement of objects. For example,
#           3124 is one possible permutation of the digits 1, 2, 3 and 4. If
#           all of the permutations are listed numerically or alphabetically,
#           we call it lexicographic order. The lexicographic permutations of
#           0, 1 and 2 are:
#
#           012   021   102   120   201   210
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   2783915460
#
# Notes:

#
def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq] # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            for m in permutate(part):
                temp.append(seq[k:k+1] + m)
    return temp

if __name__ == '__main__':

    list1 = [0,1,2]
    list2 = [0,1,2,3,4,5,6,7, 8, 9]

    print permutate(list1)
    print permutate(list2)[999999]
