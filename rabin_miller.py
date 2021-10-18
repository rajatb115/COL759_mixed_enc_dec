from random import randrange, getrandbits

debug = True

def check_prime(n,k):
    
    # checking if n is even prime or 3
    if(n==2 or n==3):
        return True
    
    # checking if n is invalid or odd
    if(n<=1 or n%2==0):
        return False
    
    # now find r and s such that (n-1) = r*(2^s) where r is odd
    r = n-1
    s = 0
    
    while(r%2==0):
        r=r//2
        s+=1
    
    if debug:
        print("n :",n)
        print("r :",r)
        print("s :",s)
        print("(n-1) = r*(2^s) : ("+str(n-1)+") =",str(r)+"*(2^"+str(s)+")")
    
    # perform k test
    for _ in range(k):
        # generate a random number
        random_number = randrange(2,n-1)
        
        # get (random_numner^r) (mod n)
        x = pow(random_number,r,n)
        
        # if x is not 1 or -1  
        if(x!=1 and x!=n-1):
            
            # check for random_number^((2^j)r) = -1 (mod n)
            j = 1
            while(j<=s-1 and x!=n-1):
                x = pow(x,2,n)
                
                if(x==1):
                    return False
                
                j=j+1
            
            if (x!=n-1):
                return False
    
    return True

def generate_prime(k):
    p = getrandbits(k)
    p |= (1 << k - 1) | 1
    return p

def generate_strong_prime(k):
    prime = 4
    
    while(check_prime(prime,k)==False):
        prime = generate_prime(k)
    
    return prime

if(debug):
    print("\nprime number :",generate_strong_prime(10))

