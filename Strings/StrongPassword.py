# https://media-exp1.licdn.com/dms/document/C561FAQFETb7OKvOXnQ/feedshare-document-pdf-analyzed/0/1643763349601?e=1643868000&v=beta&t=pHeYq-lGDaoeMG6CpTHkwpIwJwg7B9vRTJnUBFbHFTI

a="m@d31nindia"
b=len(a)
sp=['#','!','@','$','_']
splch,num,low,upp=0,0,0,0
if(8<=b<=25):
    # if(a in sp):
    #     splch+=1
    for i in a:
        if(i in sp):
            splch+=1
        if(i.islower()):
            low+=1
        if(i.isupper()):
            upp+=1
        if(i.isdigit()):
            num+=1

    print(splch)
    print(low)
    print(upp)
    print(num)
    if((splch>=1) and (num>=2) and (low>=1) and (upp>=1)):
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Password is short/long")