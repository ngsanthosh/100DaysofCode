class Solution:
    def convertFive(self,n):
        #Code here

        #O(n) solution
        # nn=list(str(n))
        # # print(nn)
        # for i in range(len(nn)):
        #     if(nn[i]=='0'):
        #         nn[i]='5'
                
        # # print(nn)
        # return int("".join(nn))
        
        ##O(n) solution - But Optimal Approach
        copy=n
        power=1
        while(n>0):
            digit=n%10
            if(digit==0):
                copy+=power*5
            power*=10
            n//=10
        return copy