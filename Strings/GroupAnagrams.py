# https://leetcode.com/problems/group-anagrams/

# T - O(n L log L) S- O(nL) where L is the length of each string
from collections import defaultdi
strs=["eat","tea","tan","ate","nat","bat"]
anag = defaultdict(list)
for stu in strs:
    anag[tuple(sorted(stu))].append(stu)
print(anag)
print ([v for v in anag.values()])

# T - O(n L) S- O(26*L)~O(1) where L is the length of each string
anag= defaultdict(list)
for stu in strs:
    count = [0]*26
    for i in stu:
        count[ord(i)-ord('a')]+=1
    anag[tuple(count)].append(stu)
print (anag.values())