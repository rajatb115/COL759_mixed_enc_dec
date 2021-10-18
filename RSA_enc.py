from random import randrange, getrandbits
import sys
import math
import random
import rabin_miller

debug = True

def encryption(p_text, pub_key):
    n,e = pub_key
    
    # finding optimal block size
    block_sz = 0
    
    # 26^block_sz < n find the max block_sz possible 
    while (26**block_sz<=n):
        block_sz+=1
        
    
    