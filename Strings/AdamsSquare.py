# The Algo of the program goes like this, if a reverse of the square of a number is equal to the 
# reverse of the number itself
# then the number is said to be adams number

# Example: 12
# 12x12=144
# 21x21=441
# thus if 144 is reversed we get 441 thus 12 is adams number

a=int(input("Enter the number"))
sq1=a**2

tocmp=str(sq1)[::-1]
# print(tocmp)
b=str(a)[::-1]
# print(b)
tocmp2=int(b)**2
# print(tocmp2)

print(int(tocmp)==tocmp2)