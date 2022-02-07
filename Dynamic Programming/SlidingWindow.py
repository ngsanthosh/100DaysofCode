# https://www.hackerrank.com/challenges/the-birthday-bar/problem


# Actually we traverse through all of the window and find the sum of each window and if it is equal to the sum
# then we increment the count

# #Optimal
# the same above process but we dont find sum in every window, we just move the window a step and subract the left 
# most number that was in the previous window



#My brute force approach
def birthday(s, d, m):
    count=0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            count+=1
    return count

# Optimal solution: https://www.youtube.com/watch?v=9fTnK0ulCXM

