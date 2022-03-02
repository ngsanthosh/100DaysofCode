# https://practice.geeksforgeeks.org/problems/find-the-odd-occurence4820/1#

#User function Template for python3
from collections import Counter
import enum
class Solution:
    def getOddOccurrence(self, arr, n):
        # code here '

        # O(n) - Time and O(n) - Space
        # dic=Counter(arr)
        # # print(dic)
        # b=dict(dic)
        # # print(list(dic))
        # final=0
        # li1=list(b.keys())
        # li2=list(b.values())
        # # print(li1,li2)
        # i,j=0,0
        # for i in range(len(li2)):
        #     # print(li2[i])
        #     if((li2[i]%2)!=0):
        #         # print()
        #         # print("Work",i)
        #         return li1[i]
        

        # O(n) - Time and O(1) - Space
        a=0
        # b=1
        # while not a>=len(arr) and not b>=len(arr):
        #     c=bin(arr[a]).replace("0b","") ^ bin(arr[b]).replace("0b","")
        #     a=c
        #     b=b+1
        for i in arr:
            a^=i
        return a
            
        
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends