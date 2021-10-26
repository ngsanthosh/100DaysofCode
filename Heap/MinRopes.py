# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1


from heapq import heappop, heappush, heapify

def minCost(ropes):
    if not ropes: return 0
    if len(ropes) == 1: return ropes[0]
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        a, b = heappop(ropes), heappop(ropes)
        cost += a+b
        if ropes:
            heappush(ropes, a+b)
    return cost

arr=[4,3,2,6]
print(minCost(arr))