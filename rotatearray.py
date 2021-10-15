# first the array/list from back till k elements is reversed and then 
# the remaining elements that is from first to n-k-1 is reversed, Finally 
# as a whole array/list is reversed, so that we get the array/list rotated

a=[1,2,3,4,5]
n=5
k=2

reverse(a,n-1,n-k)
reverse(a,n-k-1,0)
reverse(a,0,n-1)

def reverse(a,l,h):
    pass
