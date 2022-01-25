class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        fstr=""
        # cmpit=""
        s=s.lower()
        
        # s1=
        
        for i in s:
            if i.isalnum():
                fstr+=i
                
#         for j in s:
#             if j.isalpha():
#                 cmpit+=j
        # if(len(fstr)==1):
        #     return False
          
        # print(fstr)
        # print(cmpit)
        return fstr[::-1]==fstr
            
        
        
        
        