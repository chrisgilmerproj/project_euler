from math import *

def isPrime(num):
    if type(num) != int: return False
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    return not any(num % i == 0 for i in range(3, int(sqrt(num))+1, 2))

def prime_factors(num):
    if num == 1: return [num]
    if isPrime(num): return [num]
    
    powers = []
    limit = (num/2)+1
    i = 2
    
    while i <= limit:
        while num % i == 0:
            if not powers.__contains__(i): # No repeats
                powers.append(i)
            num = num/i
        i += 1
        if num == 1: break
    return powers

#def factorial(num):
#    number = int(num)
#    if number == 0:
#        return 1 # This is an important point to remember, 0! = 1
#    else:
#        return reduce(lambda i,j : i*j, range(1,number+1))

def factorial(x):
    return (1 if x==0 else x * fact(x-1))

def all_factors(num):
    if num == 1: return [num]
    if isPrime(num): return [num]
    
    powers = []
    limit = (num/2)+1
    i = 1
    
    while i <= limit:
    	if num % i == 0:
            powers.append(i)
	i += 1
    return powers

def binary(i):
    b = ''
    while i > 0:
        j = i & 1
        b = str(j) + b
        i >>= 1
    return b

#############################

def triagonal(num):
    return num*(num+1)/2

def isTriagonal(num):
    tri = (-1 + sqrt(1 + 8*num))/2
    if tri % 1 == 0:
        return True
    else:
        return False

def square(num):
    return num*num

def isSquare(num):
    square = sqrt(num)
    if square % 1 == 0:
        return True
    else:
        return False

def pentagonal(num):
    return num*(3*num-1)/2

def isPentagonal(num):
    pent = (1 + sqrt(1 + 24*num))/6
    if pent % 1 == 0:
        return True
    else:
        return False

def hexagonal(num):
    return num*(2*num-1)

def isHexagonal(num):
    hexa = (1 + sqrt(1 + 8*num))/4
    if hexa % 1 == 0:
        return True
    else:
        return False

def heptagonal(num):
    return num*(5*num-3)/2

def isHeptagonal(num):
    hepta = (3 + sqrt(9 + 40*num))/10
    if hepta % 1 == 0:
        return True
    else:
        return False

def octagonal(num):
    return num*(3*num-2)

def isOctagonal(num):
    octa = (2 + sqrt(4 + 12*num))/6
    if octa % 1 == 0:
        return True
    else:
        return False


#############################

def spiral(size):
    spiral = []

    for i in range(size):
        spiral.append([0]*size)

    x = size-1
    y = 0
    
    i = size*size

    xupper = size-1
    yupper = size-1
    xlower = 0
    ylower = 0


    while i >= 1:
        if spiral[y][x] == 0:
            spiral[y][x] = i

        if y == ylower and x > xlower:
                x -= 1
                if x == xlower:
                    ylower += 1
        elif x == xlower and y < yupper:
                y += 1
                if y == yupper:
                    xlower += 1
        elif y == yupper and x < xupper:
                x += 1
                if x == xupper:
                    yupper -= 1
        elif x == xupper and y > ylower:
                y -= 1
                if y == ylower:
                    xupper -= 1
        i -= 1

    return spiral

#############################

def isPandigital(num):
    word = list(str(num))
    if len(word) > 10:
        return False
    else:
        word.sort()
        pnum = int(''.join(word))
        if len(word) == 1 and pnum == 1:
            return True
        if len(word) == 2 and pnum == 12:
            return True
        if len(word) == 3 and pnum == 123:
            return True
        if len(word) == 4 and pnum == 1234:
            return True
        if len(word) == 5 and pnum == 12345:
            return True
        if len(word) == 6 and pnum == 123456:
            return True
        if len(word) == 7 and pnum == 1234567:
            return True
        if len(word) == 8 and pnum == 12345678:
            return True
        if (len(word) == 9 or len(word) == 10) and pnum == 123456789:
            return True
        else:
            return False

#############################

def all_perms(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))
    
