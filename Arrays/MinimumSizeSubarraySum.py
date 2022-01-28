# https://leetcode.com/problems/minimum-size-subarray-sum/
# https://www.youtube.com/watch?v=aYqYMIqZx5s&ab_channel=NeetCode

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low, total= 0,0
        res=len(nums)+1
        
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                res=min(right-low+1,res)
                total-=nums[low]
                low+=1
            
        return 0 if res==len(nums)+1 else res
            
        