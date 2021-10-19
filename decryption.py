# decryption of the message done by user B
import vigenere
import RSA_dec
import RSA_enc


# step 1 : read the message file (c,k_)
fp = open("cipher.txt",'r')
c = fp.readline()[:-1]
k_ = fp.readline()
fp.close()

if(debug):
    print("c :",c)
    print("k_ :",k_)

# step 2: 