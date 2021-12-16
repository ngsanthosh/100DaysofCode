# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Algo: we look for the maximum depth of the tree with using recursion with finding 1 + left node recursively and 
# right node recursively. Finally we return them as a result, in this way if no root is found we return 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))