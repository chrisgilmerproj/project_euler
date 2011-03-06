# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #023
#
# Problem:  Find the sum of all the positive integers which cannot be written
#           as the sum of two abundant numbers.
#
# Hint:     A perfect number is a number for which the sum of its proper
#           divisors is exactly equal to the number. For example, the sum
#           of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
#           which means that 28 is a perfect number.
#
#           A number whose proper divisors are less than the number is called
#           deficient and a number whose proper divisors exceed the number is
#           called abundant.
#
#           As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
#           the smallest number that can be written as the sum of two abundant
#           numbers is 24. By mathematical analysis, it can be shown that all
#           integers greater than 28123 can be written as the sum of two
#           abundant numbers. However, this upper limit cannot be reduced any
#           further by analysis even though it is known that the greatest number
#           that cannot be expressed as the sum of two abundant numbers is less
#           than this limit.
#
# Written by Chris Gilmer
# Solved:   10/21/2008
# Answer:   4179871
#
# Notes:

from factor import *

def check_perfect(num):
    """Return -1 if num is deficient, 0 if perfect, +1 if abundant"""
    return cmp(sum(all_factors(num)),num)

if __name__ == '__main__':

    lower = 1
    upper = 28123
    abundant_list = []

    for i in range(lower,upper+1):
        if check_perfect(i) == 1:
            abundant_list.append(i)

    print 'Number of abundant numbers: %d' % len(abundant_list)

    total = 0
    
    for i in range(lower,upper+1):
        isSum = False
        for num in abundant_list:
            if abundant_list.__contains__(i - num):
                isSum = True
                break
            if num > i:
                break
        if not isSum:
	    total += i
	if i % 1000 == 0 or i == upper:
            print i, total

#Number of abundant numbers: 6965
#1000 240492
#2000 573153
#3000 989657
#4000 1490743
#5000 2035227
#6000 2621368
#7000 3054693
#8000 3353255
#9000 3590893
#10000 3731004
#11000 3805333
#12000 3828725
#13000 3916276
#14000 3997248
#15000 4039939
#16000 4070867
#17000 4087054
#18000 4122206
#19000 4140643
#20000 4159710
#21000 4179871
#22000 4179871
#23000 4179871
#24000 4179871
#25000 4179871
#26000 4179871
#27000 4179871
#28000 4179871
#28123 4179871
