# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #042
#
# Problem:  Using euler042.txt, a 16K text file containing nearly two-thousand common
#           English words, how many are triangle words?
#
# Hint:     The nth term of the sequence of triangle numbers is given by,
#           tn = n(n+1)/2; so the first ten triangle numbers are:
#
#           1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#           By converting each letter in a word to a number corresponding to
#           its alphabetical position and adding these values we form a word
#           value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
#           If the word value is a triangle number then we shall call the word a
#           triangle word.
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   162
#
# Notes:

from math import *

def triagonal(num):
    return num*(num+1)/2

def isTriagonal(num):
    tri = (-1 + sqrt(1 + 8*num))/2
    if tri % 1 == 0:
        return True
    else:
        return False

def replace(text,dic):
    for i, j in dic.iteritems():  
        text = text.replace(i, j)
    return text

if __name__ == '__main__':

    words = []

    file = open('euler042.txt','r')
    for line in file:
        words.extend(((line.replace('"','')).replace('\n','')).split(','))

    count = 0

    alph = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}

    words.sort()

    for item in words:
        add = 0
        for each in list(item):
            add += int(replace(each,alph))
        if isTriagonal(add):
            count += 1

    print count

    file.close()
