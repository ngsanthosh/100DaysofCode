a=int(input("Enter the number"))
sq1=a**2

tocmp=str(sq1)[::-1]
# print(tocmp)
b=str(a)[::-1]
# print(b)
tocmp2=int(b)**2
# print(tocmp2)

print(int(tocmp)==tocmp2)