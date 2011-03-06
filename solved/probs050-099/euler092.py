# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #092
#
# Problem:  How many starting numbers below ten million will arrive at 89?
#
# Hint:     A number chain is created by continuously adding the square of the
#           digits in a number to form a new number until it has been seen before.
#
#           For example,
#
#           44 -> 32 -> 13 -> 10 -> 1 -> 1
#           85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
#           Therefore any chain that arrives at 1 or 89 will become stuck in
#           an endless loop. What is most amazing is that EVERY starting number
#           will eventually arrive at 1 or 89.
#
# Written by Chris Gilmer
# Solved:   12/10/2008
# Answer:   8581146
#
# Notes:

if __name__ == '__main__':

    limit = 10000000
    num = 1
    count = 0
    final_num = 0

    while num < limit:

        chain = []
        current_num = num
        repeat = False
        
        while not repeat:
            str_num = list(str(current_num))
            final_num = 0
            for item in str_num:
                final_num += int(item)**2
            if final_num == 1 or final_num == 89:
                repeat = True
            chain.append(final_num)
            current_num = final_num
            
        if final_num == 89:
            count += 1
            if count%100000 == 0: print count,'\t',num,chain

        num += 1
        
    print count
