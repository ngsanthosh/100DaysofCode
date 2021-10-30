# The primary idea is that....we go to every node and then we swap the right and left pointer to that node 
# if both right and left exist.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root==None):
            return None
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.right
            root.right=root.left
            root.left=temp
            return root