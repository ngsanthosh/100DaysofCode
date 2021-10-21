# Given array input [10, 3, 5, 6, 2] output this: [180, 600, 360, 300, 900]
# Algo: for first element product of all except first element, similarly for second element product of all except 
# second element
# Rule - Division is not allowed 


def arrayProduct(arr,n):
    output=[0]*n
    left=1
    right=1
    for i in range(n):
        output[i]=left
        left*=arr[i]
    for i in range(n-1,-1,-1):
        output[i]*=right
        right*=arr[i]
    print(output)

if __name__=='__main__':
    arr=[10, 3, 5, 6, 2]
    arrayProduct(arr,len(arr))
