import sys
def findLeaders(arr,n):
    max_value=-sys.maxsize -1
    for i in range(n-1,-1,-1):
        if(max_value<arr[i]):
            max_value=arr[i]
            print(max_value)
        
findLeaders([16, 17, 4, 3, 5, 2],6)        
