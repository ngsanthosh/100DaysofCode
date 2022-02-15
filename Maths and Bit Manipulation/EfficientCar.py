a=int(input())
lst=[]
for i in range(a):
    b=str(input()).split(' ')
    lst.append(b)
print(lst)
vals=[]

for i in lst:
    res=int(i[1])/int(i[0])
    vals.append(res)
    
resss=vals.index(max(vals))+1
print(resss)