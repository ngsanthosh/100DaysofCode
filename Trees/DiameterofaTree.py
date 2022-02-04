# https://leetcode.com/problems/diameter-of-binary-tree/

# https://www.youtube.com/watch?v=bkxqA8Rfv04


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res=[0]
        
        def deefs(root):
            if not root:
                return -1
            left = deefs(root.left)
            right= deefs(root.right)
            
            res[0]=max(res[0],2+left+right)
            
            return 1+max(left,right)
        
        deefs(root)
        
        return res[0]
        

