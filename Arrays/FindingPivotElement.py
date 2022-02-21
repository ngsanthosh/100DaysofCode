class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     leftsum=0
        #     rightsum=0
        #     lum=i
        #     while lum<len(nums):
        #         rightsum+=nums[lum]
        #         lum+=1
        #     while lum>=0:
        #         print("I prob",lum)
        #         leftsum+=nums[lum]
        #         lum-=1
        #     print(leftsum,rightsum)
        #     if leftsum==rightsum:
        #         return i
        # else:
        #     return -1
        
        total = sum(nums) # O(n)
        
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1