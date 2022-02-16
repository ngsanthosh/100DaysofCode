# https://leetcode.com/problems/valid-perfect-square/


# O(sqrt(n)) for brute force approach
# O(log n) solution using binary search intution
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # a=[x*x for x in range(num+1)]
        # print(a)
        # print(num)
        # return True if (num in a) else False
        
        l, r = 1 , num
        
        while l<=r:
            mid = (l+r) // 2
            
            if(mid*mid>num):
                r=mid-1
            elif(mid*mid<num):
                l=mid+1
            else:
                return True
        return False
                
            
        