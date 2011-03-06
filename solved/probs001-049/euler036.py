# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #036
#
# Problem: Find the sum of all numbers, less than one million, 
#          which are palindromic in base 10 and base 2.
#
# Hint:    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Written by Chris Gilmer
# Solved: 10/21/2008
# Answer: 872187
#
# Notes: A way to reverse an integer string is int(str(num)[::-1])
#        1    x 9    = 9
#        91   x 99   = 9009
#        913  x 993  = 906609
#        9901 x 9999 = 99000099

from factor import *

if __name__ == '__main__':

    upper = 1000000
    total = 0
    for num in range(1,upper+1):
        bnum = binary(num)
        if int(str(num)[::-1]) == num and str(bnum)[::-1] == str(bnum):
		total += num
		print num, bnum
	
    print total

#1 1
#3 11
#5 101
#7 111
#9 1001
#33 100001
#99 1100011
#313 100111001
#585 1001001001
#717 1011001101
#7447 1110100010111
#9009 10001100110001
#15351 11101111110111
#32223 111110111011111
#39993 1001110000111001
#53235 1100111111110011
#53835 1101001001001011
#73737 10010000000001001
#585585 10001110111101110001
