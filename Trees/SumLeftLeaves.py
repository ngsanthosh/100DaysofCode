# Given the root of a binary tree, return the sum of all left leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total=0
    isleft=False
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:      
        
        if(root is None):
            return None
        elif(not root.left and not root.right and self.isleft):
            self.total+=root.val
            return None
            
        self.isleft=True
        self.sumOfLeftLeaves(root.left)
        self.isleft=False
        self.sumOfLeftLeaves(root.right)
        return self.total
        