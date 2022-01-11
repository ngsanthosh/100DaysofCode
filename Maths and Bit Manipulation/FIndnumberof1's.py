#BruteForce

class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        a=bin(n)
        return (str(a).count('1'))
        
    
        # return a.count("1")
        
        