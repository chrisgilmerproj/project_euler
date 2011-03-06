# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #094
#
# Problem:  Find the sum of the perimeters of every almost equilateral triangle
#           with integral side lengths and area and whose perimeters do not
#           exceed one billion (1,000,000,000).
#
# Hint:     It is easily proved that no equilateral triangle exists with
#           integral length sides and integral area. However, the almost
#           equilateral triangle 5-5-6 has an area of 12 square units.
#
#           We shall define an almost equilateral triangle to be a triangle
#           for which two sides are equal and the third differs by no more
#           than one unit.
#
# Written by Chris Gilmer
# Solved:   
# Answer:   
#
# Notes:

from math import *
from decimal import *

if __name__ == '__main__':

    #getcontext().prec = 12
    D = Decimal

    perimeter = 0
    perimeter_limit = 1000000000
    perimeter_sum = 0

    n = D("2.0")

    while perimeter < perimeter_limit:

        # Change the precision as needed to keep decimal places
        if perimeter < 10000: getcontext().prec = 9
        elif perimeter < 100000: getcontext().prec = 12
        elif perimeter < 10000000: getcontext().prec = 15
        else: getcontext().prec = 18

        base = n + D("1.0")                 # the base
        base_2 = base/D("2.0")              # 1/2 the base
        
        inv_cos = D(str(acos(base_2/n)))    # inverse cosine
        tan_h = D(str(tan(inv_cos)))        # tangent
        height = base_2*tan_h               # the height
        
        area = base_2*height                # the area
        perimeter = n*D("3.0") + D("1.0")   # the perimeter
        
        if area%D("1.0") == 0 and perimeter < perimeter_limit:
            perimeter_sum += perimeter
            print 'Sides %s-%s-%s, Area: %s, Perimeter: %s, Perimeter Sum: %s' % (n,n,n+1,area, perimeter, perimeter_sum)

        n += D("1.0")

    print perimeter_sum
