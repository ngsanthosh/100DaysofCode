# Refer CODES channel

n=int(input("Enter the number of test cases"))
dic={}
for i in range(n):
    inp=input()
    lst=inp.split(" ")
    dic[lst[0]]=lst[1]

search=input("Enter the search term")
print(dic)
print(dic[search])