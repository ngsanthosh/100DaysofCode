'''Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.
Example: 
Input: 19
Output: true
Explanation: 
1pow2 + 9pow2 = 82
8pow2 + 2pow2 = 68
6pow2 + 8pow2 = 100
1pow2 + 0pow2 + 0pow2 = 1'''


def next_num(n):
    total=0
    while n>0:
        n, rem = divmod(n, 10)
        total+=rem**2
    return total

def happynum(n):
    slowp=n
    fastp=next_num(n)

    while fastp!=1 and fastp != slowp:
        slowp=next_num(n)
        fastp=next_num(next_num(n))
    return fastp==1


