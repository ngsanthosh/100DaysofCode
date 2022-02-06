#Given an number replace all 0's with 1's 

#O(log n) is appreciated

#But the below code is O(n) 👇
a=204
a=list(str(a))
for i in range(len(a)):
    if(a[i]=="0"):
        a[i]="1"

print("".join(a))