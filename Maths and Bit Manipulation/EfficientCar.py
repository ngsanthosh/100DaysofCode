# https://media-exp1.licdn.com/dms/document/C561FAQFLPz38ZnJaEg/feedshare-document-pdf-analyzed/0/1644905865713?e=1645002000&v=beta&t=ttjJhc9UtuvB8YzqwO-y4o2WnbBq6s3Lbtz9vRWJHqo

a=int(input())
lst=[]
for i in range(a):
    b=str(input()).split(' ')
    lst.append(b)
print(lst)
vals=[]

for i in lst:
    res=int(i[1])/int(i[0])
    vals.append(res)
    
resss=vals.index(max(vals))+1
print(resss)