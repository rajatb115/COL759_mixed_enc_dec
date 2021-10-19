from random import randrange, getrandbits
import sys
import math
import random
# import rabin_miller

debug = True
max_chr = 26
ct_list = []

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
    
def find_c_text(c,block_sz):
    txt = ""
    j= block_sz
    
    while(j>=0):
        ch = chr(c//(26**j)+ord("A"))
        c = c - (c//(26**j))*(26**j)
        j-=1
        txt = ch + txt
    # print(block_sz)
    # print(txt)
    return txt[::-1]
    
def decryption(p_text, priv_key):
    n,d = priv_key
    
    # finding optimal block size
    block_sz = 0
    
    # 26^block_sz < n find the max block_sz possible 
    while (26**block_sz<=n):
        block_sz+=1
    
    # print(block_sz)
    pt_list = find_block(p_text,block_sz)
    
    et_list = []
    
    for i in pt_list:
        m = find_m(i)
        
        # if(debug):
            # print(m)
        
        c = pow(m,d,n)
        ct_list.append(c)
        ans = find_c_text(c,block_sz+1)
        # print(c," , ",ans)
        et_list.append(ans)

    # print(ct_list)
    enc = ""
    for i in et_list:
        enc+=i
    return enc
  

if(debug):
    print(decryption("HBKBAAZBBAAAJQWAAATFIBAA",(28471,18227)))
