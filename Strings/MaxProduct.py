# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def nocommon(str1,str2):
            for i in str1:
                if(i in str2):
                    return False
            return True
        maxx=0
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                if(nocommon(words[x],words[y])):
                    maxx=max(maxx,len(words[x])*len(words[y]))
                    
                    
        return maxx
                
            