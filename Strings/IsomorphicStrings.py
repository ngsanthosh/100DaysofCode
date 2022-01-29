# https://leetcode.com/problems/isomorphic-strings/

# https://www.youtube.com/watch?v=7yF-U1hLEqQ

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ltr,rtl={},{}
        
        for i in range(len(t)):
            c1=s[i]
            c2=t[i]
            
            if((c1 in ltr and ltr[c1]!=c2) or (c2 in rtl and rtl[c2]!=c1)):
                return False
            
            ltr[c1]=c2
            rtl[c2]=c1
            
            
        return True
            