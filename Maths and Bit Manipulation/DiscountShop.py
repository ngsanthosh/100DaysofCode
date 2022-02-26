a=int(input("Enter the number of items bought"))
prices=[]
for i in range(a):
    b=int(input())
    prices.append(b)
total=0
for j in prices:
    print(total)
    if j>=1000:
        print(",",j,"1000")
        total+=(j*(50/100)) #or else (j-(j*(50/100))) is also correct     
    elif j>500:
        print(",",j,"500")
        total+=(j-(j*(25/100)))
    elif j>400:
        print(",",j,"400")
        total+=(j-(j*(20/100)))
    else:
        print(",",j,"excepted")
        total+=j
        
if total>2000:
    total-=100
    
print(total)
        