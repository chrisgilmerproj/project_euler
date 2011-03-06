# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #022
#
# Problem:  What is the total of all the name scores in the file?
#
# Hint:     Using euler022.txt, a 46K text file containing over five-thousand
#           first names, begin by sorting it into alphabetical order. Then
#           working out the alphabetical value for each name, multiply this
#           value by its alphabetical position in the list to obtain a name score.
#
#           For example, when the list is sorted into alphabetical order, COLIN,
#           which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
#           list. So, COLIN would obtain a score of 938 53 = 49714.
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   871198282
#
# Notes:

def replace(text,dic):
    for i, j in dic.iteritems():  
        text = text.replace(i, j)
    return text

if __name__ == '__main__':

    names = []

    file = open('euler022.txt','r')
    for line in file:
        names.extend(((line.replace('"','')).replace('\n','')).split(','))

    total = 0
    count = 1

    alph = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}

    names.sort()

    for item in names:
        add = 0
        for each in list(item):
            add += int(replace(each,alph))
        total += add * count
        count += 1

    print total

    file.close()
