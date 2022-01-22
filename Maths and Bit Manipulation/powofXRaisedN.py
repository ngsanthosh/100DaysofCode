#https://leetcode.com/problems/powx-n/


# For Other approach without using built in function, refer the photo along with name capture.png

# Algo: The algo of the capture file program is that, for e.g. instead of doing 2pow7 2 times 7 ,
# we do ((2 times 3) * 2 + 1 time 2) .. We generally split and find the power resultt...
import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x,n)
        