from collections import defaultdi
strs=["eat","tea","tan","ate","nat","bat"]
anag = defaultdict(list)
for stu in strs:
    anag[tuple(sorted(stu))].append(stu)
print(anag)
print ([v for v in anag.values()])