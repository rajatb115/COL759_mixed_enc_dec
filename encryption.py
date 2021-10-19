# encryption of the message done by user A
import vigenere

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

# Step 2: read vigenere cipher key
fp = open(input("Enter the file name(contain vigenere key) with location: "),'r')
k = fp.readline()
fp.close()

# Step 3: encryption using vigenere cipher cs <- E(m, k)
cs = vigenere.encrypt(message,k)
if(debug):
    print("vigenere kye :",k)
    print("message :",message)
    print("cs :",cs)


# reading user A private keys and user B public keys