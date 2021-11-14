# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        que=[]
        que.append(root)
        result=[]
        
        while que:
            n=len(que)
            for i in range(1,n+1):
                current=que[0]
                que.pop(0)
                if i==n :
                    result.append(current.val)
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
        return result