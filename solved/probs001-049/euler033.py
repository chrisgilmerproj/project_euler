# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #033
#
# Problem:  If the product of these four fractions is given in its lowest common
#           terms, find the value of the denominator.
#
# Hint:     The fraction 49/98 is a curious fraction, as an inexperienced
#           mathematician in attempting to simplify it may incorrectly believe
#           that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
#           We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#           There are exactly four non-trivial examples of this type of fraction,
#           less than one in value, and containing two digits in the numerator and
#           denominator.
#
# Written by Chris Gilmer
# Solved:   10/29/2008
# Answer:   100
#
# Notes:

if __name__ == '__main__':

    numerator_list = []
    denominator_list = []

    for numerator in range(10,100):
        for denominator in range(10,100):

            div = float(numerator)/float(denominator)
            new_div = 0.0
            numerator_word = list(str(numerator))
            denominator_word = list(str(denominator))
            
            if numerator_word[0] == denominator_word[1]:
                new_numerator = float(numerator_word[1])
                new_denominator = float(denominator_word[0])
                if new_numerator != 0.0 and new_denominator != 0.0:
                    new_div = new_numerator/new_denominator
            elif numerator_word[1] == denominator_word[0]:
                new_numerator = float(numerator_word[0])
                new_denominator = float(denominator_word[1])
                if new_numerator != 0.0 and new_denominator != 0.0:
                    new_div = new_numerator/new_denominator

            if div == new_div and numerator != denominator and div < 1.0:
                numerator_list.append(int(new_numerator))
                denominator_list.append(int(new_denominator))
                print '\t%s/%s = %s/%s = %s' % (numerator, denominator, int(new_numerator), int(new_denominator), div)

    product_numerator = reduce(lambda i,j: i*j, numerator_list)
    product_denominator = reduce(lambda i,j: i*j, denominator_list)
    print '\n\tThe products of these fractions is: %s/%s' % (product_numerator, product_denominator)
    print '\tWith the lowest common demonimator of: %s\n' % (product_denominator/product_numerator)

    
