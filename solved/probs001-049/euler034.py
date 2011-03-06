# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #034
#
# Problem:  Find the sum of all numbers which are equal to the sum of the
#           factorial of their digits.
#
# Hint:     145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#           Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# Written by Chris Gilmer
# Solved:   10/21/2008
# Answer:   40730, made of [145, 40585]
#
# Notes:

def factorial(num):
    number = int(num)
    if number == 0:
        return 1 # This is an important point to remember, 0! = 1
    else:
        return reduce(lambda i,j : i*j, range(1,number+1))

if __name__ == '__main__':

    f_list = []
    total = 0
    upper = 1000000
    
    for number in range(3,upper+1):
        if number == reduce(lambda i,j: i+factorial(j), [0]+list(str(number))):
            f_list.append(number)
            total += number

    print f_list
    print total

##    print factorial(0) # 1
##    print factorial(1) # 1
##    print factorial(2) # 2
##    print factorial(3) # 6
##    print factorial(4) # 24
##    print factorial(5) # 120
##    print factorial(6) # 720
##    print factorial(7) # 5040
##    print factorial(8) # 40320
##    print factorial(9) # 362880
