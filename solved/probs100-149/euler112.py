# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #112
#
# Problem:  Find the least number for which the proportion of bouncy numbers is
#           exactly 99%.
#
# Hint:     Working from left-to-right if no digit is exceeded by the digit to
#           its left it is called an increasing number; for example, 134468.
#
#           Similarly if no digit is exceeded by the digit to its right it is
#           called a decreasing number; for example, 66420.
#
#           We shall call a positive integer that is neither increasing nor
#           decreasing a "bouncy" number; for example, 155349.
#
#           Clearly there cannot be any bouncy numbers below one-hundred, but
#           just over half of the numbers below one-thousand (525) are bouncy.
#           In fact, the least number for which the proportion of bouncy numbers
#           first reaches 50% is 538.
#
#           Surprisingly, bouncy numbers become more and more common and by the
#           time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
# Written by Chris Gilmer
# Solved:   12/17/2008
# Answer:   1587000
#
# Notes:    The ratio here refers to all numbers, not just numbers above 99

def bounce(n):
    word = list(str(n))

    btype = ''

    for i in range(0,len(word)-1):
        if word[i+1] > word[i]:
            if btype == '' or btype == 'i':
                btype = 'i'
            else:
                btype = 'b'
                break
        elif word[i+1] < word[i]:
            if btype == '' or btype == 'd':
                btype = 'd'
            else:
                btype = 'b'
                break
    
    if btype == 'b':
        return True
    else:
        return False

if __name__ == '__main__':

    count = 0.0
    b_ratio = 0.0
    n = 100

    while n < 2000000:
        if bounce(n):
            count += 1.0
            b_ratio = count/n
            if b_ratio == 0.99:
                print n, count, b_ratio
                break
        n += 1

    


