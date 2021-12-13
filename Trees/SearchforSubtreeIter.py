# The iterative approach of Searching a node in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
                if(root.val>val):
                    root=root.left
                else:
                    root=root.right
                    
        return None if not root else root
        
#         if not root:
#             return None
#         if root.val == val:
#             return root
        
#         if root.val > val :
#             return self.searchBST(root.left, val)
        
#         if root.val < val :
#             return self.searchBST(root.right, val)

            
                    
        