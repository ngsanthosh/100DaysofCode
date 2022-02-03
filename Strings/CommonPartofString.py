# https://www.geeksforgeeks.org/print-common-characters-two-strings-alphabetical-order-2/

# here we traverse through one of the string and compare if it is there on the another string or not, if yes 
# then we add it to resultant string and finally we sort the resultant string and print it

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