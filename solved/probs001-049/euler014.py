# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #014
#
# Problem:  
#
# Hint:     
#
# Written by Chris Gilmer
# Solved:   10/16/2008
# Answer:   837799 with sequence of 524 numbers
#
# Notes:
 
if __name__ == '__main__':

    limit = 1000000
    seq_len = 0

    for n in range(2,limit):
        seq = []
        j = n
        count = 0
        while j != 1:
            if j%2 == 0:
                j = j/2
            else:
                j = 3*j + 1
            count += 1
        if count > seq_len:
            seq_len = count
            top_num = n
            print top_num, seq_len
        
