# Given an number find the digital sum that is the final sum on recursively doing it and ending with 
# one digit number....(Otthapadai)!!

def yesh(a):
    # a=246
    b=list(str(a))

    c=[int(x) for x in b]
    res=sum(c)
    # print(res)
    # print(len(str(sum(c)))!=1)
    if(len(str(sum(c)))!=1):
        yesh(res)
    else:
        print("Finally",res)

# print("Executin")
b=input()
yesh(b)v