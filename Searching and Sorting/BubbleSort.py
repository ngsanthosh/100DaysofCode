

def bubb(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            try:
                if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
            except:
                pass

a=[3,1,11,4,80,19,36,41,2]

bubb(a)

print(a)