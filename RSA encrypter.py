import os
import sys
# Python3 program Miller-Rabin primality test
import random
import math
import numpy
from unidecode import unidecode
from SHA1hash import sha1
 
# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
     
    # Initialize result
    res = 1;
     
    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;
 
# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
     
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);
 
    # Compute a^d % n
    x = power(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    # Return composite
    return False;
 
# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime(n, k):
     
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Iterate given number of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;
 

# Python3 program to find multiplicative modulo
# inverse using Extended Euclid algorithm.
 
# Global Variables
x, y = 0, 1
 
# Function for extended Euclidean Algorithm
 
 
def gcdExtended(a, b):
    global x, y
 
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 
 
def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        return
 
    else:
 
        # m is added to handle negative x
        res = (x % M + M) % M
        return res

# Driver Code
# Number of iterations
 
# This code is contributed by mits

not_possible = []
k = 1000

while True:
    p = os.urandom(128)
    if (p not in not_possible):
        if isPrime(int.from_bytes(p, sys.byteorder), k):
            print(f"p = {int.from_bytes(p, sys.byteorder)}")
            while True:
                q = os.urandom(128)
                if p != q:
                    if (q not in not_possible):
                        if isPrime(int.from_bytes(q, sys.byteorder), k):
                            print(f"q = {int.from_bytes(q, sys.byteorder)}")
                            break
                        not_possible.append(q)
            break
        not_possible.append(p)

p = int.from_bytes(p, sys.byteorder)
q = int.from_bytes(q, sys.byteorder)

n = p * q

print(f'n = {n}')

yp = p - 1
yq = q - 1

yn = numpy.lcm(yp, yq)

print(f'yn = {yn}')

efound = False

for e in range(65537, yn):
    if math.gcd(e, yn) == 1:
        efound = True
        break

if efound != True:
    for e in range(2, 65537, -1):
        if math.gcd(e, yn) == 1:
            efound = True
            break

print(f'e = {e}')

d = modInverse(e, yn)

print(f'd = {d}')

M = unidecode(input('Message to be encrypted: '))

M_array = []

for i in M:
    M_array.append(ord(i))

c_array = []

for i in M_array:
    c_array.append((i ** e) % n)

print(c_array)

decrypted_array = []

for i in c_array:
    decrypted_array.append(pow(i, d, n))

decrypted = ''

for i in decrypted_array:
    decrypted += chr(i)

print(decrypted)