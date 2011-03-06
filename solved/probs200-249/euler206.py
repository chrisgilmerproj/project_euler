# -*- coding: utf-8 -*-
# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #206
#
# Problem:  Find the unique positive integer whose square has the
#           form 1_2_3_4_5_6_7_8_9_0, where each '_' is a single digit.
#
# Hint:     
#
# Written by Chris Gilmer
# Solved:   10/21/2008
# Answer:   1389019170
#
# Notes:

from math import sqrt

if __name__ == '__main__':

    #print sqrt(1020304050607080900) # Lower Bound
    #print sqrt(1929394959697989990) # Upper Bound

    i =   1389019170#1010101010
    end = 1389026624
    
    while i <= end:
        word = list(str(i*i))
        if word[0] == '1':
            if word[2] == '2':
                if word[4] == '3':
                    if word[6] == '4':
                        if word[8] == '5':
                            if word[10] == '6':
                                if word[12] == '7':
                                    if word[14] == '8':
                                        print '8',i,word
                                        if word[16] == '9':
                                            print '9',i,word
                                            if word[18] == '0':
                                                print 'Winner',i,word
                                                break
        i += 1
                                            
#Winner 1389019170 ['1', '9', '2', '9', '3', '7', '4', '2', '5', '4', '6', '2', '7', '4', '8', '8', '9', '0', '0']
