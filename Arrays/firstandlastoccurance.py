# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left =  self.binsearch(nums,target,True)
        right =  self.binsearch(nums,target,False)
        
        return [left,right]
    def binsearch(self, nums,target,leffo):
        l=0
        r=len(nums)-1
        i=-1
        
        while l<=r:
            m=(l+r)//2
            if(target > nums[m]):
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                i=m
                if leffo:
                    r=m-1
                else:
                    l=m+1
        return i
                