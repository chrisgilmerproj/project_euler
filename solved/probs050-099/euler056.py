# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #056
#
# Problem:  Considering natural numbers of the form, a^b, where a, b 100, what is the 
#           maximum digital sum?
#
# Hint:     A googol (10^100) is a massive number: one followed by one-hundred zeros; 
#           100^100 is almost unimaginably large: one followed by two-hundred zeros. 
#           Despite their size, the sum of the digits in each number is only 1.
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   972
#
# Notes:

if __name__ == '__main__':

    a_max = 100
    b_max = 100
    
    digital_max = 0
    
    for a in range(1,a_max+1):
        for b in range(1,b_max+1):
	    num = a**b
            numword = list(str(num))
	    digital_sum = 0
	    for element in numword:
	        digital_sum += int(element)
	    if digital_sum > digital_max:
	        digital_max = digital_sum
		#print digital_max

    print '\n\tThe largest digital sum for the given range is: %s\n' % digital_max
