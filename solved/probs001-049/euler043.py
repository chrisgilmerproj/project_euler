# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #043
#
# Problem:  Find the sum of all 0 to 9 pandigital numbers with this property.
#
# Hint:     The number, 1406357289, is a 0 to 9 pandigital number because it is
#           made up of each of the digits 0 to 9 in some order, but it also has
#           a rather interesting sub-string divisibility property.
#
#           Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on.
#           In this way, we note the following:
#
#           * d_(2)d_(3)d_(4)=406 is divisible by 2
#           * d_(3)d_(4)d_(5)=063 is divisible by 3
#           * d_(4)d_(5)d_(6)=635 is divisible by 5
#           * d_(5)d_(6)d_(7)=357 is divisible by 7
#           * d_(6)d_(7)d_(8)=572 is divisible by 11
#           * d_(7)d_(8)d_(9)=728 is divisible by 13
#           * d_(8)d_(9)d_(10)=289 is divisible by 17
#
# Written by Chris Gilmer
# Solved:   12/10/2008
# Answer:   16695334890
#
# Notes:

from factor import *

def all_perms(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

if __name__ == '__main__':

    pandigital = ['0','1','2','3','4','5','6','7','8','9']
    total = 0

    for str_num in all_perms(pandigital):

        d1 = int(''.join(str_num[1:4]))
        d2 = int(''.join(str_num[2:5]))
        d3 = int(''.join(str_num[3:6]))
        d4 = int(''.join(str_num[4:7]))
        d5 = int(''.join(str_num[5:8]))
        d6 = int(''.join(str_num[6:9]))
        d7 = int(''.join(str_num[7:10]))
        if d1%2 == 0:
            if d2%3 == 0:
                if d3%5 == 0:
                    if d4%7 == 0:
                        if d5%11 == 0:
                            if d6%13 == 0:
                                if d7%17 == 0:
                                    int_num = int(''.join(str_num))
                                    print '\t',int_num,d1,d2,d3,d4,d5,d6,d7
                                    total += int_num

    print '\nThe sum of all pandigital numbers with partial prime number divisibility is: %s' % total
