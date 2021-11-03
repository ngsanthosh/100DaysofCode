def getSplitpoint(arr,n):
    leftsum=0
    rightsum=0
    for i in range(n):
        leftsum+=arr[i]
    
    for i in range(n-1,-1,-1):
        rightsum+=arr[i]
        leftsum-=arr[i]
        if leftsum==rightsum:
            return i
    return -1

if __name__=='__main__':
    arr=[1,2,3,4,5,5]
    point=getSplitpoint(arr,len(arr))
    if(point==-1 or point==len(arr)):
        print("Split cannot be done")
    else:
        for i in range(len(arr)):
            if i==point:
                print("\n")
            print(arr[i]),
