# Print the staircase pattern by just running an for loop also the for loop i in range from 1 to last index + 1 
# Then we print spaces for n-i and # for i times for the current iteration of 'i' that matter.

# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'#'*(i))