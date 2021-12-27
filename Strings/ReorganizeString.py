# https://leetcode.com/problems/reorganize-string/

class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        samp=[]
        for i,c in sorted((s.count(c),c) for c in set(s)):
            if i >(n+1)/2:
                return ""
            samp.extend(i*c)
        res = [None]*n
        res[::2]=samp[n//2:]
        res[1::2]=samp[:n//2]
        # print(str(res))
        return ''.join(res)