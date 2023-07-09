import os
import sys
# Python3 program Miller-Rabin primality test
import random
import math
import numpy
from SHA1hash import sha1
from MGF1mask import mgf1
 
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

def generate_padding_string(k, mLen, hLen):
    padding_length = k - mLen - 2 * hLen - 2
    padding_string = b'\x00' * padding_length
    return padding_string

k = math.ceil(n.bit_length() / 8)
M = input('Message to be encrypted: ').encode()
mLen = len(M)

L = "atumalaca".encode()
lHash = sha1(L)
hLen = len(lHash)
PS = generate_padding_string(k, mLen, hLen)

DB = lHash + PS + b'\x01' + M

seed = os.urandom(hLen)

dbMask = mgf1(seed, k - hLen - 1)

maskedDB = bytes([a ^ b for a, b in zip(DB, dbMask)])

seedMask = mgf1(maskedDB, hLen)

maskedSeed = bytes([a ^ b for a, b in zip(seed, seedMask)])

print('maskedSeed original')

for i in maskedSeed:
    print(i)

print('maskedDB original')

for i in maskedDB:
    print(i)

EM = b'\x00' + maskedSeed + maskedDB

EM_length = len(EM)


integer_data = int.from_bytes(EM, byteorder='big')

crypted = pow(integer_data, e, n)

print(crypted)

decrypted = pow(crypted, d, n)

decrypted_bytes = decrypted.to_bytes(EM_length, byteorder= 'big')

lHash = sha1(L)

maskedSeed = decrypted_bytes[1 : hLen + 1]
maskedDB = decrypted_bytes[hLen + 1 : ]

seedMask = mgf1(maskedDB, hLen)

seed = bytes([a ^ b for a, b in zip(maskedSeed, seedMask)])

dbMask = mgf1(seed, k - hLen - 1)

DB = bytes([a ^ b for a, b in zip(maskedDB, dbMask)])

lHashverify = DB[ : hLen]

remainder = DB[hLen : ]

print('remainder', remainder)

counter = 0

for i in remainder:
    if i == 1:
        counter += 1
        break
    counter += 1

print('tamanho remainder', len(remainder))

print('contador', counter)

M = remainder[counter : ]

print(M)

print('message: ', M.decode())