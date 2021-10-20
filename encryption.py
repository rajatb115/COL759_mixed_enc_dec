# encryption of the message done by user A
import vigenere
import RSA_dec
import RSA_enc
import RSA_dec_new
import RSA_enc_new

debug = True

def get_message(fp):
    fp_read = fp.readline()
    message = ""
    
    while(fp_read):
        for i in range(len(fp_read)):
            if((ord(fp_read[i])>=ord('a') and ord(fp_read[i])<=ord('z')) or (ord(fp_read[i])>=ord('A') and ord(fp_read[i])<=ord('Z'))):
                message+=fp_read[i].upper()
        fp_read = fp.readline()
    return message

# step 1 : read the message file
fp = open(input("Enter the file name(contain message) with location: "),'r')
message = get_message(fp)
fp.close()

if(debug):
    print("message :",message)

# Step 2: read vigenere cipher key
fp = open(input("Enter the file name(contain vigenere key) with location: "),'r')
k = fp.readline()
fp.close()

# Step 3: encryption using vigenere cipher cs <- E(m, k)
cs = vigenere.encrypt(message,k)
if(debug):
    print("vigenere kye :",k)
    print("cs :",cs)

# Step 4: reading A's private key and B's public keys
fp = open("privateA/private_key_A.txt",'r')
ska = (int(fp.readline()[:-1]),int(fp.readline()))
fp.close()

fp = open("publicAB/public_key_B.txt",'r')
pkb = (int(fp.readline()[:-1]),int(fp.readline()))
fp.close()

if (debug):
    print("ska :",ska)
    print("pkb :",pkb)

# Step 5: decrypting cs and k using ska (D(cs, k, ska))
cs__ = RSA_dec_new.decryption(cs,ska)
k__ = RSA_dec_new.decryption(k,ska)

if (debug):
    print("cs__ :",cs__)
    print("k__ :",k__)

# Step 6: encrypting cs'' k'' using pkb (E(D(cs, k, ska), pkb))
c = RSA_enc.encryption(cs__,pkb)
k_ = RSA_enc.encryption(k__,pkb)

if(debug):
    print("c :",c )
    print("k_ :",k_)

# Step 7: write the c and k' in a file
fp = open("cipher.txt",'w')
fp.write(c+"\n")
fp.write(k_)
fp.close()

# wallah we are ready for decryption
