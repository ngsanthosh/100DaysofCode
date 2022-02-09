from collections import Counter

a="999 aa 22aa"

b=Counter(a)
out=""
print(b)
digit=[]
alp=[]

for i in b.keys():
    if i.isalpha():
        alp.append(b[i])
    elif i.isdigit():
        digit.append(b[i])

print(digit, alp)
get1=max(digit)
get2=max(alp)

ind=abs(get1-get2)
print("asdf",ind)


g=max(b.values())
print(g)
tosee=a[ind]
print(tosee)
for i in range(len(a)):
    if(a[i]==tosee):
        pass
    # if(a[i]!=tosee):
    #     out+=a[i]
    elif(a[i]==" "):
        out+="$"
    elif(a[i]!=tosee):
        out+=a[i]

print(out)