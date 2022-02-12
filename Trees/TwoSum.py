#Time Limit Exceeded Error!!



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # ges=[]
    def findTarget(self, root, k):
        ges=[]
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        
        def calc():
            print(ges)
            
            for i in range(len(ges)):
                for j in range(i+1,len(ges)):
                    print("YEss",k)
                    if(ges[i]+ges[j]==k):  
                        print("???")
                        return True
            else:
                
                return False
            
            
        def mainn(root, k):
            if not root:
                return None

            mainn(root.left, k)
            ges.append(root.val)
            mainn(root.right, k)


        # mainn()
        mainn(root, k)
        print(ges)
        if calc():
            return True
        else:
            return False