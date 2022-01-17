# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack1=[]
        stack2=[]
        result=[]
        stack1.append(root)

        while (len(stack1)>0) or (len(stack2)>0):
            while(len(stack1)>0):
                temp=stack1.pop()
                result.append(temp.val)
                if(temp.right is not None):
                    stack2.append(temp.right)
                if(temp.left is not None):
                    stack2.append(temp.left)
            while(len(stack2)>0):
                temp=stack2.pop()
                result.append(temp.val)
                if(temp.left is not None):
                    stack1.append(temp.left)
                if(temp.right is not None):
                    stack1.append(temp.right)
                    
        return result
        