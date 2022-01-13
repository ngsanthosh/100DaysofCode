#My brute force approach
def birthday(s, d, m):
    count=0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            count+=1
    return count