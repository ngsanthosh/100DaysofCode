def nonRepeatingString(string):
    index=[0]*26
    count=[0]*26
    
    for i in range(len(string)):
        x=string[i]
        
        count[ord(x)-97]+=1
        index[ord(x)-97]=i

    min_value=sys.maxsize
    value=0
    for i in range(len(count)):
        if count[i]==1:
            if index[i]<min_value:
                min_value=index[i]
                value=i
    print("Index of the value {} and char is {}".format(min_value,str(chr(value+97))))

if __name__=='__main__':
    string="santhosh"
    nonRepeatingString(string)
        
