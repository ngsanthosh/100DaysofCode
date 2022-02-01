# Given an start and ending range, we should find all the intersting numbers within that, 

# An intresting number is a number 
#  we should find the count of odd numbers and even numbers in the current string/Number,

#  If oddCount in that number is even and EvenCount in that number is odd, then a number is said to Be intresting number


start=2
end=200
count=0
for i in range(start, end+1):
    ocount,ecount=0,0
    s=str(i)
    for i in s:
        if(int(i)%2==0):
            ecount+=1
        else:
            ocount+=1

    if((ecount%2==1) and (ocount%2==0)):
        count+=1

print(count)