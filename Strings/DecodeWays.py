#We use Dynamic Programming here...we take each index value of string one by one and solve for it.

# https://leetcode.com/problems/decode-ways/

# This is the way in which the string can be decoded in all different possible ways

class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(i):
            if i in dic:
                return dic[i]
            if i >= len(s):
                return 1
            res = 0
            if 1 <= int(s[i]) <= 9:
                res += helper(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += helper(i+2)
            dic[i] = res
            return res
        dic = {}
        return helper(0) if s else 0