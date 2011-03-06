# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #007
#
# Problem:  What is the 10001st prime number?
#
# Hint:     By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#           we can see that the 6th prime is 13.
#
# Written by Chris Gilmer
# Solved:   10/15/2008
# Answer:   104743
#
# Notes:    any() returns a true or false statement based on conditions given

import math

# Prime number check
def prime(num):
    if num == 2: return True
    if num < 2 or num%2 == 0: return False
    return not any(num%i == 0 for i in range(3, int(math.sqrt(num))+1, 2))

if __name__ == '__main__':
    
    n = 10001
    count = 2       # This is true only if you start with 2 or 3
    cur_num = 3     # Here we start with 3
    cur_prime = 3   # The current number is 3

    while count < n:
        cur_num += 2
        if prime(cur_num):
            cur_prime = cur_num
            count += 1

    print '\n\tThe nth prime for n=%d is %s' % (n, cur_prime)
