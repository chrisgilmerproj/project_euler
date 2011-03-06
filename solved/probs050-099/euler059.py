# This is a problem from the Project Euler Website
# http://projecteuler.net/
#
# Euler Problem #059
#
# Problem:  Your task has been made easy, as the encryption key consists of
#           three lower case characters. Using cipher1.txt (right click and
#           'Save Link/Target As...'), a file containing the encrypted ASCII
#           codes, and the knowledge that the plain text must contain common
#           English words, decrypt the message and find the sum of the ASCII
#           values in the original text.
#
# Hint:     Each character on a computer is assigned a unique code and the
#           preferred standard is ASCII (American Standard Code for Information
#           Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
#           lowercase k = 107.
#
#           A modern encryption method is to take a text file, convert the bytes
#           to ASCII, then XOR each byte with a given value, taken from a secret
#           key. The advantage with the XOR function is that using the same
#           encryption key on the cipher text, restores the plain text; for
#           example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
#           For unbreakable encryption, the key is the same length as the plain
#           text message, and the key is made up of random bytes. The user would
#           keep the encrypted message and the encryption key in different
#           locations, and without both "halves", it is impossible to decrypt
#           the message.
#
#           Unfortunately, this method is impractical for most users, so the
#           modified method is to use a password as a key. If the password is
#           shorter than the message, which is likely, the key is repeated
#           cyclically throughout the message. The balance for this method is
#           using a sufficiently long password key for security, but short
#           enough to be memorable.
#
# Written by Chris Gilmer
# Solved:   12/15/2008
# Answer:   107359
#
# Notes: 

from curses.ascii import *

if __name__ == '__main__':

    # Import txt file
    file = open('euler059.txt','r')
    for line in file:
        encrypted_message = line.replace('\n','').split(',')
    file.close()

    original_message = range(len(encrypted_message))

    # Use brute force to check all passwords
    # ascii lower case letters are 97 - 122
    for a in range(97,123):
        for b in range(97,123):
            for c in range(97,123):
                step = 1

                # Decrypt using code sequence
                for i in range(0,len(encrypted_message)):
                    if step == 1:
                        original_message[i] = int(encrypted_message[i]) ^ a
                    else:
                        if step == 2:
                            original_message[i] = int(encrypted_message[i]) ^ b
                        else:
                            original_message[i] = int(encrypted_message[i]) ^ c

                    # 32 is ascii for space
                    # Break out of loop if ascii falls out of range
                    if original_message[i] < 32 or original_message[i] > 122:
                        break

                    # Track which code letter is being used
                    step += 1
                    if step == 4: step = 1

                    # If code has been decrypted completely with ASCII characters
                    if i == len(encrypted_message) - 1:
                        print "\n\tPassword: ", chr(a), chr(b), chr(c)

                        message = ""
                        ascii_count = 0
                        
                        for i in range(0,len(encrypted_message)):
                            message += chr(original_message[i])
                            ascii_count += original_message[i]
                        print "\tMessage: ", message
                        print "\tASCII Count: ", ascii_count
