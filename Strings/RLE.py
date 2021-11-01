# Run Length Encoding


def RLE(string):
    count=0
    s=""
    i=0
    n=len(string)
    while(i<n):
        count=1
        while(i+1<n and string[i]==string[i+1]):
            count+=1
            i+=1
        
        s+=str(count)+string[i]
        i+=1
    return s

if __name__=='__main__':
    string="AAAAABBBBBBCCCCC"
    print(RLE(string))