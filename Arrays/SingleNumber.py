# Given a non-empty array of integers, every element appears twice except for one. Find that single one.


def getOddOccurence(arr):
    res=0
    for i in arr:
        res=res^i
    return res

if __name__=='__main__':
    arr=[1,1,2,2,3,3,4]
    print(getOddOccurence(arr))

#OUTPUT -> 4