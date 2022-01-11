# https://leetcode.com/problems/find-peak-element/

# O(log n) approach - https://extraimage.info/pix/image.RM1W8B

#O(n) approach using built in function
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a=sorted(nums)
        # b=a.sort()
        # print(a)
        # print(nums)
        return nums.index(a[-1])