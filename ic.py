
debug = True

def index_of_concidence(s):
    cnt=[]
    for i in range(26):
        cnt.append(0)
    
    for i in range(len(s)):
        cnt[ord(s[i])-ord("A")]+=1
    
    txt_length = len(s)
    
    # using formula IC = (sum_i (f_i*(f_i-1)))/(n*(n-1))
    IC = 0
    for i in range(26):
        IC = IC + cnt[i]*(cnt[i]-1)
    
    IC = IC/(txt_length * (txt_length - 1))
    
    return IC

if (debug):
    print(index_of_concidence("hihowareyouIamgoodramsaidsowhatistheproblemwithyourpartofthecode".upper()))