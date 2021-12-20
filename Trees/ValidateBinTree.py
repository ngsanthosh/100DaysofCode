# https://leetcode.com/problems/validate-binary-search-tree/

import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        lower = -sys.maxsize
        upper = sys.maxsize
             
        stack = [(root, lower,upper)]
        
        while stack:
            
            root, lower, upper = stack.pop()
            
            if(not root):
                continue
            val = root.val
            if(val<=lower or val>=upper):
                return False
            else:
                stack.append((root.left, lower, val))
                stack.append((root.right, val, upper))
            
        return True