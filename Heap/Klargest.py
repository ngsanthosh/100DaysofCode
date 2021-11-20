# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashit=Counter(nums)
        return heapq.nlargest(k, hashit.keys(),key= hashit.get)
        print(hashit.get)