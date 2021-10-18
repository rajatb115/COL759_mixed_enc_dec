import rabin_miller
import gmpy2
import random

debug = True

def find_strong_prime(prime_bits):

    s = rabin_miller.generate_strong_prime(prime_bits)
    while(not gmpy2.is_prime(s)):
        s = rabin_miller.generate_strong_prime(prime_bits)

    t = rabin_miller.generate_strong_prime(prime_bits)
    while(not gmpy2.is_prime(t)):
        t = rabin_miller.generate_strong_prime(prime_bits)

    while(s==t):
        t = rabin_miller.generate_strong_prime(prime_bits)
        while(not gmpy2.is_prime(t)):
            t = rabin_miller.generate_strong_prime(prime_bits)

    if(debug):
        print("s =",s)
        print("t =",t)

    isPrime = False

    # r=2it+1 find the first prime r, that satisfies this condition. 
    i = random.randint(0,100)
    while(not isPrime):
        r = 2*i*t+1
        i+=1

        if(gmpy2.is_prime(r)):
            isPrime = True

    if(debug):
        print("r =",r)

    # p0=2(s*r−2(mod r))s−1 
    p0 = 2*(pow(s,r-2,r))*s-1

    if(debug):
        print("p_0 =",p0)

    isPrime = False
    p=0
    j=random.randint(0,100)
    while (not isPrime):
        p=p0+2*j*r*s
        j=j+1
        if (gmpy2.is_prime(p)):
            isPrime=True

    if(debug):
        print("strong prime =",p)

    return p
