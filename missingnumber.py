#Program to find the missing number in a given list of n series
#Find the missing number
num=10
list1=[1,9,3,5,6,7,8,4,10]
sum1=0
actual=int(num*(num+1)/2)

# for i in range(num+1):
#     actual+=i
for i in list1:
    sum1+=i

print(actual-sum1)
    
