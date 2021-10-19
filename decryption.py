# decryption of the message done by user B
import vigenere
import RSA_dec
import RSA_enc

debug = True

# step 1 : read the message file (c,k_)
fp = open("cipher.txt",'r')
c = fp.readline()[:-1]
k_ = fp.readline()
fp.close()

if(debug):
    print("c :",c)
    print("k_ :",k_)

# step 2: read secret key of B and public key of A
fp = open("privateB/private_key_B.txt",'r')
skb = (int(fp.readline()[:-1]),int(fp.readline()))
fp.close()

fp = open("publicAB/public_key_A.txt",'r')
pka = (int(fp.readline()[:-1]),int(fp.readline()))
fp.close()

if (debug):
    print("ska :",skb)
    print("pkb :",pka)

# step 3: decrypting c and k_ using skb (D(c, k_, skb))
cs__ = RSA_dec.decryption(c,skb)
k__ = RSA_dec.decryption(k_,skb)

if(debug):
    print("cs__ :",cs__)
    print("k__ :",k__)

# step 4: encrypting cs'' k'' using pka (E(D(c, k_, skb), pka))
cs = RSA_enc.encryption(cs__,pka)
k = RSA_enc.encryption(k__,pka)

if(debug):
    print("cs :",cs)
    print("k :",k)

# step 5: decryption using vigenere cipher m <- D(cs, k)
m = vigenere.decrypt(cs,k)

if(debug):
    print("m :",m)
    
# step 6: write the cs and k in a file
fp = open("plain.txt",'w')
fp.write(m+"\n")
fp.write(k)
fp.close()
