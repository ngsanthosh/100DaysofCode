#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        # check=[]
        # aa=list(A)
        # for i in aa:
        #     print(i)
        #     check.append(B.index(i))
        #     aa.remove(i)
            
        # return (check==check.sort())
        
        # check=list(A)
        # print(check)
        # test=[]
        
        # for i in B:
        #     if i in check:
        #         test.append(i)
        # print(test)
        
        # for i in A:
        #     if(i==len(A)-1):
        #         return False
        #     for j in B:
        #         if(j==len(B)-1):
        #             return False
        #         if(j==)
        i,j=0,0
        while True:
            if(i==len(A)):
                return True
                
            elif(j==len(B)):
                # print(j)
                return False
            # print("I value",i)
            if(A[i]==B[j]):
                # print(A[i],B[j])
                
                i+=1
                j+=1
                continue
            else:
                # if(j==len(B)-1):
                #      return False
                j+=1
                continue
        # print(i,len(A)-1)
        
            
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends