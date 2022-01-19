class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        if(not root or (not root.left and not root.right)):
            return 1
        currsum=0
        if root:
            if root.left:
                currsum+=root.left.data
            if root.right:
                currsum+=root.right.data
            if(currsum==root.data and self.isSumProperty(root.left) and self.isSumProperty(root.right)):          
                return 1
            else:
                return 0