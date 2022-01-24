# https://leetcode.com/problems/group-anagrams/

# T - O(n L log L) S- O(nL) where L is the length of each string
from collections import defaultdi
strs=["eat","tea","tan","ate","nat","bat"]
anag = defaultdict(list)
for stu in strs:
    anag[tuple(sorted(stu))].append(stu)
print(anag)
print ([v for v in anag.values()])