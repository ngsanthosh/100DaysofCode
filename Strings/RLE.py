# Run Length Encoding

# We first traverse every character in the string and check the number of times it has occured
# and we return "5A3B5C"

# Sadly this algorithm takes O(n^2) time 😥


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
        # print(i)
        i+=1
    return s

if __name__=='__main__':
    string="AAAAABBBBBBCCCCC"
    print(RLE(string))