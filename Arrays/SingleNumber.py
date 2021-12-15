# Given a non-empty array of integers, every element appears twice except for one. Find that single one.


# Algo: We are just finding the xor of it, like xor of anything that arrives only once in 
# an array is 1 that is, if 0 xor 1 is 1 while 1 xor something else(other then 1) is not 1, so 
# we return the result

def getOddOccurence(arr):
    res=0
    for i in arr:
        res=res^i
    return res

if __name__=='__main__':
    arr=[1,1,2,2,3,3,4]
    print(getOddOccurence(arr))

#OUTPUT -> 4