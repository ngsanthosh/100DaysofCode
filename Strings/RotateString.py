


a="ghftd:1246"
b=a.split(':')
# print(b)
sum=0
for i in b[1]:
    sum=sum+(int(i)*int(i))
if(sum%2==0):
    # print("even")
    tem=b[0][1:len(a)-1]
    # print(tem)
    res=tem+b[0][0]
else:
    # print("odd")
    tem=b[0][2:len(a)-2]
    res=tem+b[0][0]+b[0][1]

print(res)
