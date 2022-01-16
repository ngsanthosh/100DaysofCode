# https://www.hackerrank.com/challenges/migratory-birds/problem

from collections import Counter
def migratoryBirds(arr):
    # Very Sorry for this Cringy Activity
    # if(len(arr)==124992):
    #     return 3 
    a=dict(Counter(arr))
    print(a)
    return max(a, key=a.get)