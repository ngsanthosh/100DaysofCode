# https://leetcode.com/problems/valid-palindrome/

# In this we use the python inbuilt function isalnum() which is used to check if a character is a alphanumeric character
# or not. also we use lower() function to convert the given string into lowercase. then finally we reverse the string and 
# compare it with the original array 


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
            
        
        
        
        