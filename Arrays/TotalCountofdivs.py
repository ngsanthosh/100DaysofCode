# https://practice.geeksforgeeks.org/problems/total-count2415/1#

class Solution:
    def totalCount(self, arr, n, k):
        # code here
        count=0
        for i in arr:
            if(i%k!=0):
                d=(i//k)+1
            else:
                d=(i//k)
            count+=d
        return count