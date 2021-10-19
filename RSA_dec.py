from random import randrange, getrandbits
import sys
import math
import random
# import rabin_miller

debug = True
max_chr = 26
ct_list = [24369, 727, 15297, 23133]
    
def solve(ct_block,n,d):
    c = pow(ct_block,d,n)
    # print(c)
    txt = ""
    j=1
    temp=c
    while(c!=0):
        # print(j," ",c%(max_chr**j))
        txt = txt+ str(c%(max_chr**j))
        c = c - c%(max_chr**j)
        c=c//(max_chr**(j-1))
        j+=1
    return txt[::-1]

def decryption(et_list, keys):
    n,d = keys
    dt_list = []
    for ct_block in ct_list:
        # We can use CRT to decrypt each block here
        ans = solve(int(ct_block),n,d)
        dt_list.append(ans)
    return dt_list


if(debug):
    # use private key d and public key n for decryption
    print(decryption(ct_list,(28471,18227)))