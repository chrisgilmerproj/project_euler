# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #017
#
# Problem:  If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#           how many letters would be used?
#
# Hint:     If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
#           there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#           NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
#           contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use
#           of "and" when writing out numbers is in compliance with British usage.
#
# Written by Chris Gilmer
# Solved:   10/20/2008
# Answer:   21124
#
# Notes:

def replace(text,dic):
    for i, j in dic.iteritems():  
        text = text.replace(i, j)
    return text

if __name__ == '__main__':

    # Dictionary Values
    ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    teens = {'10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
    tens = {'2':'twenty ', '3':'thirty ', '4':'forty ', '5':'fifty ', '6':'sixty ', '7':'seventy ', '8':'eighty ', '9':'ninety '}
    
    total = 0
    upper = 1000

    for num in range(1,upper+1):
        word = list(str(num))
        sentence = ''
        
        if len(word) >= 4 and int(word[-4]) >= 1:
            sentence += replace(word[-4],ones)+' thousand '
            
        if len(word) >= 3 and int(word[-3]) >= 1:
            if int(word[-2]) == 0 and int(word[-1]) == 0:
                sentence += replace(word[-3],ones)+' hundred '
            else:
                sentence += replace(word[-3],ones)+' hundred and '
            
        if len(word) >= 2 and int(word[-2]) >= 2:
            sentence += replace(word[-2],tens)
            
        if len(word) >= 2 and int(word[-2]) == 1:
            sentence += replace(word[-2]+word[-1],teens)
            
        if int(word[-1]) >= 1:
            if len(word) >= 2 and int(word[-2]) == 1:
                sentence += ''
            else:
                sentence += replace(word[-1],ones)
                
        #print sentence
        
        total+=len(sentence.replace(' ',''))

    print '\n\tThe total number of letters used in writing out every number from 1 to %s is %s\n' % (upper,total)
