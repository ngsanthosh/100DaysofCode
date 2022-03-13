# Run Length Encoding

# We first traverse every character in the string and check the number of times it has occured
# and we return "5A3B5C"

# Sadly this algorithm takes O(n^2) time 😥

# Update: Fortunately the below algo takes only O(n) time

def encode(arr):
    # Code here
    ret = ""
    count=1
    s=len(arr)
    
    if(s==1):
        return arr+"1"
    arr=arr+' '
    for i in range(1,s+1):
        if(arr[i]!=arr[i-1]):
            ret+=arr[i-1]+str(count)
            count=0
            # pass
        count+=1
    return ret