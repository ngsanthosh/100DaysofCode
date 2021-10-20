# Here we need to split the array in a point where, the sum of left sub array and right sub array are same.
# Algo:
# The Logic goes like this,, first we calculate for the sum of all elements in the array and then we assign 
# it to the leftsum variable, then we iterate the loop from back side till first element and at every step
# we check if left sum is equal to right sum or not!! The key idea is we keep on decrementing leftsum and incrementing 
# rightsum...at a point both will be equal


def getSplitpoint(arr,n):
    leftsum=0
    rightsum=0
    for i in range(n):
        leftsum+=arr[i]
    
    for i in range(n-1,-1,-1):
        rightsum+=arr[i]
        leftsum-=arr[i]
        if leftsum==rightsum:
            return i
    return -1