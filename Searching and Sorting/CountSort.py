#User function Template for python3

#COUNT SORT - WE USE COUNT SORT WHEN UPPER BOUND LIMIT AND LOWER BOUND LIMIT IS KNOWN
class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        #No need to print the array
    
        hashm={'0':0,'1':0}
        for i in A:
            # if str(i) not in hashm:
            #     if i==0:
            #         hashm['0']=1  
            #     else:
            #         hashm['1']=1
            # else:
                if i==0:
                    hashm['0']+=1  
                else:
                    hashm['1']+=1
                
            
        # print(hashm)
        
        if(hashm['0']):
            zcou=hashm['0']
        else:
            zcou=0
        if(hashm['1']):
            ocou=hashm['1']
        else:
            ocou=0
            # ocou=hashm['1']
        # print(zcou,ocou)
        s=''
        
        arr=[0 for i in range(zcou)]
        for i in range(ocou):
            arr.append(1)
        # print(arr)
        # s+=" ".join(arr)
        # print("S is",s)
        # print(arr)
        
        
        for h in range(len(arr)):
            A[h]=arr[h]
            
        
        # print("A is",A)
            
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends