# The logic of the program is that, we take log base 2 of the given value and we check ceil
# and floor value of them..if both are same then...we can know that its an whole number is thus a 
# power of 2 definetely

import math
a=int(input("Enter the number"))

print(math.ceil(math.log2(a))==math.floor(math.log2(a)))