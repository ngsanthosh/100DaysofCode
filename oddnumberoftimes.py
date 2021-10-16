#Python program to find the number that is occuring odd number of times in a given list
# Algo:
# We use XOR operator, that if values are same then we get 0, if values are different we get 1
# so if even number of times we get zero and if odd number of times we get one. 
# Time complexity if O(n) and Space complexity is O(1)
a=[1,2,2,4,5,4,4]
fin=0

for i in a:
    fin = fin ^ i #xor() inbuilt function can also be used

print(fin)