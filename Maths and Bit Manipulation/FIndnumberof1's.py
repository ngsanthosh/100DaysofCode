# https://leetcode.com/problems/number-of-1-bits/


#BruteForce
class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        a=bin(n)
        return (str(a).count('1'))
        
    
        # return a.count("1")

#Using Bit Manipulation     
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 #Binary ANDing
            n=n>>1 #Right Shifting by 1
        return count
        
        