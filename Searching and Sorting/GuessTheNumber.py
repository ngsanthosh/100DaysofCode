#Alias of Binary Search

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1,n
        
        while 1:
            mid = (l+r)//2
            res = guess(mid)
            if(res>0):
                l=mid+1
            elif(res<0):
                r=mid-1
            else:
                return mid