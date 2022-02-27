# https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1

#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        sum1={}
        # sum2={}
        for i in A:
            if i not in sum1:
                sum1[i]=1
            else:
                sum1[i]+=1
        for i in B:
            if i not in sum1:
                sum1[i]=0
            else:
                sum1[i]-=1
        
        # print(sum1,sum2)
        # flag=0
        # h=sum1.values():
        for i in sum1.values():
            if i!=0:
                return 0
            
        # if not flag:
        #     return 1
        # else:
        #     return 0
        return 1
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends