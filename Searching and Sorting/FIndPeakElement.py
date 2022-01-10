# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a=sorted(nums)
        # b=a.sort()
        # print(a)
        # print(nums)
        return nums.index(a[-1])