import rabin_miller
import gmpy2

debug = True

prime_bits = 128

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

