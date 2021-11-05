# The idea behind this prob is that, we traverse the array from back side, and maintain a max size, that is by 
# comparing each and every element with max size. initially max size is - max size. 
# Time O(n) and space O(1)

import sys
def findLeaders(arr,n):
    max_value=-sys.maxsize -1
    for i in range(n-1,-1,-1): #Alter: for i in reversed(range(0,n)):
        if(max_value<arr[i]):
            max_value=arr[i]
            print(max_value)
        
findLeaders([16, 17, 4, 3, 5, 2],6)        
