a=[1,2,3,4,5]
n=5
k=2

reverse(a,n-1,n-k)
reverse(a,n-k-1,0)
reverse(a,0,n-1)


def reverse(a,l,h):
    