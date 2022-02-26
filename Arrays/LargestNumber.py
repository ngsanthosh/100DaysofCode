# https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # i=nums[0]
        # j=nums[1]
        
        numss=[str(h) for h in nums]
        # print(numss)
        for i in range(len(numss)):
            for j in range(i+1, len(numss)):
                # print(numss[i]+numss[j],numss[j]+numss[i])
                if(numss[i]+numss[j] > numss[j]+numss[i]):
                    continue
                else:
                    numss[i],numss[j]=numss[j],numss[i]
        return str(int("".join(numss)))