from random import randrange, getrandbits
import sys
import math
import random
# import rabin_miller

debug = True

max_chr = 26

def find_m(txt):
    m = 0
    
    j = 0
    
    # reversing the string
    txt1 = ""
    for i in txt:
        txt1= i+txt1
    
    # print(txt1)
    
    for i in txt1:
        m+=(ord(i)-ord("A"))*(max_chr**j)
        # print(m)
        j+=1
    return m

def find_block(pt,block_len):
    lis = []
    i=0
    while(i<len(pt)):
        lis.append(pt[i:min(len(pt),i+block_len)])
        i += block_len
    
    return lis
    
def find_c_text(c):
    txt = ""
    
    j=1
    
    while(c!=0):
        txt = txt+ str(c%(max_chr**j))
        c = c - c%(max_chr**j)
        c=c//(max_chr**(j-1))
        j+=1
    
    return txt
    
def encryption(p_text, pub_key):
    n,e = pub_key
    
    # finding optimal block size
    block_sz = 0
    
    # 26^block_sz < n find the max block_sz possible 
    while (26**block_sz<=n):
        block_sz+=1
        
    pt_list = find_block(p_text,block_sz)
    
    et_list = []
    
    for i in pt_list:
        m = find_m(i)
        
        if(debug):
            print(m)
        
        c = pow(m,e,n)
        
        ans = find_c_text(c)
        et_list.append(ans)
    
    enc = ""
    for i in et_list:
        enc+=i
    return enc
    
if(debug):
    print(encryption("INDIAISMYCOUNTRY",(28471,3)))