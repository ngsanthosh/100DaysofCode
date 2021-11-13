#IF you solve using examples, you will get a pattern of numbers and that will be 
# in pattern of fibonacci series. so here also the n is the step count. and finding n fibonacci series and this 
# problem is same


#recursive solution
def climb_stairs(i,n):
    if i>n:
        return 0
    if i==n:
        return 1
    return climb_stairs(i+1,n)+climb_stairs(i+2,n)

if __name__=='__main__':
    print("number of ways",climb_stairs(0,4))
    


#Dynamic Programming
def climbStairs(n):
    #However it returns 1, so the below condition is no longer needed
    # if(n==1):
    #     return 1 
    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

if __name__=='__main__':
    print("number of ways",climbStairs(4))
