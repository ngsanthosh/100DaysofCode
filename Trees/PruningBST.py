#https://leetcode.com/problems/binary-tree-pruning/


# Algo: we just traverse through each of the node and drop all the subtrees which
# only have '0's on them also we drop all 0's nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        
        if(not root.left and not root.right and root.val==0):
            return None
        return root
        