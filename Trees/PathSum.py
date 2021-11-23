# https://leetcode.com/problems/path-sum/
# Algo:
# The root of the tree is given and we need to traverse the path in which sum is equal to given target sum,
# so we check if given root is none and we keep on subracting the value of current node from the total target sum and 
# if that node has no left and right node, also if our sum counter is zero, then we return that True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum=targetSum
        if root is None:
            return False
        sum=sum-root.val
        if(root.left is None and root.right is None):
            return sum==0
        
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
    
        