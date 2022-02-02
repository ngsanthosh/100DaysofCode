# https://www.geeksforgeeks.org/print-common-characters-two-strings-alphabetical-order-2/

a="geeksforgeeks"
b="practiceforgeeks"
c=""
# ans=[]
prevlen=len(c)
for i in b:
    if(i in a):
        # if(i not in c):
            c+=i
# if(len(c)>prevlen):
#     ans.append(c)
#
# print(ans[-1])



# c=a|b
# print(c)
print("".join(sorted(c)))