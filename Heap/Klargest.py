# https://leetcode.com/problems/top-k-frequent-elements/

# ALgo: First we construct a hashmap which has the counter for all variables, then we construct a max heap 
# and in that we sort the hashtmap with key having it key as the number of times it appeared!! then we just return it

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashit=Counter(nums)
        return heapq.nlargest(k, hashit.keys(),key= hashit.get)
        print(hashit.get)