# Remove Adjacent Character

def removeAdj(string):
    string=list(string)
    s=0
    prev=None
    str_value=""
    for f in range(0,len(string)):
        if(prev!=string[f]):
            string[s]=string[f]
            s+=1
        prev=string[f]
    for i in range(s):
        str_value+=string[i]
    return str_value

if __name__=='__main__':
    string="AABAABCCC"
    print((removeAdj(string)))
            
