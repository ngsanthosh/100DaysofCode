# Given a sentence of words, reverse the words in that sentence (p.s. not letters)'

# Here we first split the string in terms of list and then we reverse the list and then again using 
# join method, we join the list and return that as output

a="I love you"

b=list(a.split(' ')) #Spliting based on space and converting to list
b.reverse() #Reverse a List
# or else
# c=b[::-1] #This also reverses a list
# print(c)
# print(b)
# result="-"
# for i in c:
#     result+= i+" "
bb=" ".join(b) #We can join a list to a string using "join" keyword
print(bb)
# print("result",result)

#OUTPUT: you love I