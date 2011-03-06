# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #079
#
# Problem:  Given that the three characters are always asked for in order, 
#           analyse the file so as to determine the shortest possible secret 
#           passcode of unknown length.
#
# Hint:     A common security method used for online banking is to ask the user
#           for three random characters from a passcode. For example, if the 
#           passcode was 531278, they may asked for the 2nd, 3rd, and 5th 
#           characters; the expected reply would be: 317.
#
#           The text file, keylog.txt, contains fifty successful login attempts.
#
# Written by Chris Gilmer
# Solved:   12/15/2008
# Answer:   73162890
#
# Notes:    Solved by hand

if __name__ == '__main__':

    login_attempts = []
    login_digits = []

    file = open('euler079.txt','r')
    for line in file: 
        new = list(line.replace('\n',''))
        if not login_attempts.__contains__(new):
	    login_attempts.append(new)
    file.close()
    
    # Solved by hand
	        
        
