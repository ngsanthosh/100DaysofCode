# https://www.youtube.com/watch?v=8i-f24YFWC4&t=256s

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # a=[i for i in range(1,len(nums)+1)]
        # print(a)
        # # result=[]
        # for i in nums:
        #     if i in a:
        #         a.remove(i)
        # return a
        
        for n in nums:
            i = abs(n) - 1
            nums[i]=-1*abs(nums[i])
        
        res=[]
        for i,v in enumerate(nums):
            if(v>0):
                res.append(i+1)
        return res
            
            
            
            
            
            
        
        
            