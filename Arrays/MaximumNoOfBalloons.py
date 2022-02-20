# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution(object):
    def maxNumberOfBalloons(self, text):
        check=Counter(text)
        
        baloon=Counter("balloon")
        res=len(text)
        for i in baloon:
            res=min(res,(check[i]//baloon[i]))
            
        return res
        
        
        