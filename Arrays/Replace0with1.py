a=204
a=list(str(a))
for i in range(len(a)):
    if(a[i]=="0"):
        a[i]="1"

print("".join(a))