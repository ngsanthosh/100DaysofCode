#Program to find the missing number in a given list of n series
#Find the missing number
# Algo--
# The sum of first n number is first found and then the given list's sum is found. 
# Then finally we will get the missing number. Note that in every iteration the loop
# should start from 1 rather 0

num=10
list1=[1,9,3,5,6,7,8,4,10]
sum1=0
actual=int(num*(num+1)/2)

# for i in range(num+1):
#     actual+=i
for i in list1:
    sum1+=i

print(actual-sum1)
    
