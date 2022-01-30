# https://leetcode.com/problems/nim-game/

# Algo: Given n number of stones, in a turn only 1 to 3 stones can be taken by a player, and so if n=4 last stone will be taken
# by opponent and i lose, so whenever there is a multiple of 4, i lose and opponent wins

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n%4==0