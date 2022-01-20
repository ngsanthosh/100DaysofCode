# given a string with alphabets and digits separeted by ':', we need to find the sum of square of 
# the digits, if that is even we perform one right rotation alphabet part alone, else if it is even then we perform 
# two right rotation on that alphabet part alone


a="ghftd:1246"
b=a.split(':')
# print(b)
sum=0
for i in b[1]:
    sum=sum+(int(i)*int(i))
if(sum%2==0):
    # print("even")
    tem=b[0][:-1]
    # print(tem)
    res=b[0][-1]+tem
else:
    # print("odd")
    tem=b[0][2:len(a)-2]
    res=tem+b[0][0]+b[0][1]

print(res)
