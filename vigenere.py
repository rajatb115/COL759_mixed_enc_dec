
debug = True

def decrypt(ct,key):
    key_len = len(key)
    ct_len = len(ct)
    
    key_as_int = [ord(i) for i in key]
    ct_as_int = [ord(i) for i in ct]
    
    plain = ''
    
    for i in range(ct_len):
        plain+=chr((ct_as_int[i]-key_as_int[i%key_len])%26+65)
    
    return plain
    
# append an extra character is not implemented yet
def encrypt(pt,key):
    key_len = len(key)
    pt_len = len(pt)
    
    # padding the extra bits with X if required
    if(pt_len%key_len != 0):
        # print(pt_len%key_len)
        pt = pt + 'X'*(pt_len%key_len)
    
    pt_len = len(pt)
    
    if (debug):
        print("plain text after padding :",pt)
    
    key_as_int = [ord(i) for i in key]
    pt_as_int = [ord(i) for i in pt]
    
    cipher = ''
    
    for i in range(pt_len):
        cipher+=chr((pt_as_int[i]+key_as_int[i%key_len])%26+65)
    
    return cipher

'''
if(debug):
    print(encrypt("BBB","CCC"))
    print(decrypt(encrypt("BBB","CCC"),"CCC"))
'''