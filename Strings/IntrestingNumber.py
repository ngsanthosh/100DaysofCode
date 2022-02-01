


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