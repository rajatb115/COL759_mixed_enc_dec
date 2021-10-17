import ic

debug = True

def find_shift_ct(ct,key_len):
    lis = []
    for i in range(key_len):
        lis.append("")
    
    for i in range(ct):
        lis[i%key_len]+=ct[i]
    
    return lis
    

def find_key_len(ct):
    
    best_len = 0
    deviation = 1
    
    # checking for length of the key
    for i in range(2,11,1):
        key_len = i
        lis = find_shift_ct(ct,key_len)
        
        IC = 0
        
        for l in lis:
            IC+=ic.index_of_concidence(l)
        
        IC = IC/key_len
        
        if(deviation > abs(IC-0.065)):
            best_len = key_len
            deviation = abs(IC-0.065)
    
    return best_len
        
def decrypt(ct):
    
    # Find the key length
    key_len = find_key_len(ct)
    
    # Find the key and the plain text
    

# append an extra character is not implemented yet
def encrypt(key,pt):
    key_len = len(key)
    pt_len = len(pt)
    
    key_as_int = [ord(i) for i in key]
    pt_as_int = [ord(i) for i in pt]
    
    cipher = ''
    
    for i in range(pt_len):
        cipher+=chr((pt_as_int[i]+key_as_int[i%key_len])%26+65)
    
    return cipher

if(debug):
    print(encrypt("BBB","AAA"))