# https://www.youtube.com/watch?v=CoptSI1qkwU


import math
a="93012562"
sub=set()

for i in range(len(a)):
    for j in range(i,len(a)+1):
            sub.add(int(a[i:j+1]))


# a=list(sorted(sub))
prob=[]

for num in sub:
    # print(num)
    for z in range(1,int(math.sqrt(num))+1):
        if(z*(z+1)==num):
            # print("pass")
            prob.append(num)
            break

print(prob)
