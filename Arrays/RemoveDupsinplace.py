# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #Meth1
        a=nums.count(val)

        for i in range(a):
            nums.remove(val)
        
        return len(nums)    

        #Meth2
        while val in nums:
            nums.remove(val)
            
        return len(nums)
        