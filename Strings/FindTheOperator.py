# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Very Very Bruteeeee force approach

# Given an expression with wrong operator of answer find the correct operator that yields the correct answer
a="999-9=111"

b=a.split("=")

# print(b)
cmp=[]

for i in b[0]:
    if i in ['+','-','*','/']:
        cmp=b[0].split(i)
        
cmp=[int(i) for i in cmp]
# print(cmp)
# print(b[1])
# print
# print("asdf",cmp[0]*cmp[1])
if(cmp[0]+cmp[1]==int(b[1])):
    print("+")
elif(cmp[0]-cmp[1]==int(b[1])):
    print("-")
elif(cmp[0]*cmp[1]==int(b[1])):
    # print("asdf",cmp[0]*cmp[1])
    print("*")
elif(cmp[0]/cmp[1]==int(b[1])):
    print("/")
else:
    print("none")
    
    
    
    
    
    
    
    
    
    