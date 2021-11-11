#recursive approach
def rodCutting(arr,length):
    if length<=0:
        return 0
    
    max_rod=-1
    
    for i in range(length):
        max_rod=max(max_rod,arr[i]+rodCutting(arr,length-(i+1)))
    return max_rod

if __name__=='__main__':
    arr=[2, 3, 7, 8, 9]
    length=5
    print("max rod",rodCutting(arr,length))
    

#dynamic Programming Approach
def rodCutting(arr,length):
    dp=[0]*(length+1)
    dp[0]=0
    for i in range(1,length+1):
        max_val=-1
        for j in range(i):
            max_val=max(max_val,arr[j]+dp[i-(j+1)])
            dp[i]=max_val
            
    return dp[length]

if __name__=='__main__':
    arr=[2, 3, 7, 8, 9]
    length=5
    print("max rod",rodCutting(arr,length))
