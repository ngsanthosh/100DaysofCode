# The logic is simple, we sort the numbers with one of the best algorithm that is of O(nlogn) time. And 
# then Pick 
# the k-1 th element


def Kthlargest(nums,k):
    n=len(nums)
    nums.sort() #We expect the inbuilt function to take the efficient time of n log n 
    return nums[k-1]


Kthlargest([5,3,6,1,4],3)