from random import randrange, getrandbits
import sys
import math
import random
import rabin_miller


debug = True

def find_mod_inv(a,m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
def generate_keys(k_length):
    # create two large prime numbers p and q
    p = rabin_miller.generate_strong_prime(k_length)
    q = rabin_miller.generate_strong_prime(k_length)
    
    # n = p * q
    n = p*q
    
    # gcd ( (p-1)(q-1) ,x) = 1
    a = (p-1)*(q-1)
    while True:
        x = random.randrange(2 ** (k_length - 1), 2 ** (k_length))
        if gcd(x, a) == 1:
            break
    
    
    # find d = modular inverse of x
    d = find_mod_inv(x, a)
    public_key = (n, x)
    private_key = (n, d)
    
    return public_key,private_key


public_key, private_key = generate_keys(128)

if(debug):
    print("public_key :",public_key)
    print("private_key :",private_key)