# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        summ,diff,s=0,0,0
        for i in range(len(gas)):
            summ=summ+gas[i]-cost[i]
            if(summ<0):
                s=i+1
                diff+=summ
                summ=0
        return s if summ+diff>=0 else -1 