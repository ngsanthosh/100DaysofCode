# Remove Adjacent Character
#Here we have two variables and use one as previous pointer and another one as current pointer
# so now we iterate and keep on comparing the characters finally avoid repeated characters and
# return the non redundant string
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
            
