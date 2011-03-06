# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #055
#
# Problem:  How many Lychrel numbers are there below ten-thousand?
#
# Hint:     If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
#           Not all numbers produce palindromes so quickly. For example,
#
#           349 + 943 = 1292
#           1292 + 2921 = 4213
#           4213 + 3124 = 7337
#
#           That is, 349 took three iterations to arrive at a palindrome.
#
#           Although no one has proved it yet, it is thought that some numbers,
#           like 196, never produce a palindrome. A number that never forms a
#           palindrome through the reverse and add process is called a Lychrel
#           number. Due to the theoretical nature of these numbers, and for the
#           purpose of this problem, we shall assume that a number is Lychrel
#           until proven otherwise. In addition you are given that for every
#           number below ten-thousand, it will either (i) become a palindrome
#           in less than fifty iterations, or, (ii) no one, with all the
#           computing power that exists, has managed so far to map it to a
#           palindrome. In fact, 10677 is the first number to be shown to
#           require over fifty iterations before producing a palindrome:
#           4668731596684224866951378664 (53 iterations, 28-digits).
#
#           Surprisingly, there are palindromic numbers that are themselves
#           Lychrel numbers; the first example is 4994.
#
#           NOTE: Wording was modified slightly on 24 April 2007 to emphasise
#           the theoretical nature of Lychrel numbers.
#
# Written by Chris Gilmer
# Solved:   12/08/2008
# Answer:   249
#
# Notes:

if __name__ == '__main__':

    i = 1
    limit = 10000

    lychrel = []
    
    while i < limit:
        palindrome = False
        count = 1
        total = i
        print i
        while palindrome == False and count < 50:
            new_i = total
            reverse_i = list(str(new_i))
            reverse_i.reverse()
            reverse_i = int(str(''.join(reverse_i)))
            
            total = new_i + reverse_i

            print "\t%s + %s = %s" % (new_i, reverse_i, total)
            
            str_total = list(str(total))
            reverse_total = list(str(total))
            reverse_total.reverse()
            
            if str_total == reverse_total:
                palindrome = True
                
            count += 1
            
        if count == 50:
            lychrel.append(i)
            print "\n\tLychrel number:", i

        i += 1
        
    print '\nThere are %s Lychrel numbers below %s' % (len(lychrel),limit)
    print 'These numbers are:', lychrel
