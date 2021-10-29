# Given the root of a binary tree, count the number of leap nodes present.
#Recursive Approach

import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.left = None
        self.right = None 
    
def insert(ptr,key):
    if(ptr is None):
        ptr=node(key)
    elif(key<=ptr.info):
        ptr.left=insert(ptr.left,key)
    elif(key>ptr.info):
        ptr.right=insert(ptr.right,key)
    return ptr

def getLeafcount(root):
    if(root==None):
        return 0
    if(root.left== None and root.right==None):
        return 1
    
    return getLeafcount(root.left)+getLeafcount(root.right)

if __name__=='__main__':
    root=None
    root=insert(root,10)
    root=insert(root,5)
    root=insert(root,15)
    root=insert(root,30)
    print(getLeafcount(root))






