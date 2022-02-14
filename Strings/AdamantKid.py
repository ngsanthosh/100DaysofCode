a="icecream"
x=4
y=10

b=len(a)
while b<y:
    a*=2
    b=len(a)
print(a)
print(a[x-1]==a[y-1])