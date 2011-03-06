# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #004
#
# Problem: Find the largest palindrome made from the product of two 3-digit numbers.
#
# Hint: A palindromic number reads the same both ways. The largest palindrome made 
#       from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Written by Chris Gilmer
# Solved: 10/14/2008
# Answer: 906609
#
# Notes: A way to reverse an integer string is int(str(num)[::-1])
#        1    x 9    = 9
#        91   x 99   = 9009
#        913  x 993  = 906609
#        9901 x 9999 = 99000099

def products(power):
    num = 0
    biggest_palindrome = 0
    mult1, mult2 = 0, 0
    
    for i in range(pow(10,power-1),pow(10,power)):
        for j in range(pow(10,power-1),pow(10,power)):
	    num = i*j
	    if int(str(num)[::-1]) == num and num > biggest_palindrome:
		biggest_palindrome = num
		mult1 = i
		mult2 = j

    print '\n\tThe largest palindrome made from the product of two %s-digit numbers:' % (power)
    print '\tThe final equation is %s x %s = %s' % (mult1, mult2, biggest_palindrome)

if __name__ == '__main__':
    #products(1)
    #products(2)
    products(3)
    #products(4)
