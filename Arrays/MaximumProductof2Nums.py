# https://practice.geeksforgeeks.org/problems/maximum-product-of-two-numbers2730/1#

class Solution:
	def maxProduct(self,arr, n):
		# code here
        # O(n logn) solution
        #a=sorted(arr)
        #return a[-1]*a[-2]

            #O(n) solution
            max1=max(arr)
            arr.remove(max1)
            max2=max(arr)
            
            return max1*max2