# a=["Raja","Bhuvanu","Babu","Geetha","Karthi","Babiu"]
def compare(str1,str2):
    # print("Comparing",str1,str2)
    i=0
    j=0
    while(i<len(str1) and j<len(str2)):
        # if(len(str1)==len(str2)):
            if(str1[i]==str2[j]):
                i+=1
                j+=1
            elif(str1[i]<str2[j]):
                return False
                break
            else:
                return True
                break
        # else:
        #     if(len(str1)>len(str2)):
        #         return True
        #     else:
        #         return False

        # return True
def sorting(a):
    count=0
    for i in range(len(a)-1):
        if(compare(a[i],a[i+1])):
            count+=1
            # print("Swapped")
            a[i],a[i+1]=a[i+1],a[i]


    return a if count==0 else sorting(a)

new=sorting(["Bhuvana","zoho","kaveri","Karthi","Babu","kavitha"])
# new=sorting(['8','15','14','1','2'])

print(new)
