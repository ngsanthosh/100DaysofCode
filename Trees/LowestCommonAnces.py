# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to check if given node is present in binary tree or not
def isNodePresent(root, node):
 
    # base case
    if root is None:
        return False
 
    # if node is found, return true
    if root == node:
        return True
 
    # return true if node is found in the left subtree or right subtree
    return isNodePresent(root.left, node) or isNodePresent(root.right, node)
 
 
# Function to find lowest common ancestor of given nodes x and y where
# both x and y are present in the binary tree.
# The function returns true if x or y is found in subtree rooted at root
# lca -> stores LCA(x, y)
def findlca(root, lca, x, y):
 
    # base case 1: return false if tree is empty
    if root is None:
        return False, lca
 
    # base case 2: return true if either x or y is found
    # with lca set to the current node
    if root == x or root == y:
        return True, root
 
    # recursively check if x or y exists in the left subtree
    left, lca = findlca(root.left, lca, x, y)
 
    # recursively check if x or y exists in the right subtree
    right, lca = findlca(root.right, lca, x, y)
 
    # if x is found in one subtree and y is found in other subtree,
    # update lca to current node
    if left and right:
        lca = root
 
    # return true if x or y is found in either left or right subtree
    return (left or right), lca
 
 
# Function to find lowest common ancestor of nodes x and y
def findLCA(root, x, y):
 
    # lca stores lowest common ancestor
    lca = None
 
    # call LCA procedure only if both x and y are present in the tree
    if isNodePresent(root, y) and isNodePresent(root, x):
        lca = findlca(root, lca, x, y)[1]
 
    # if LCA exists, print it
    if lca:
        print("LCA is", lca.data)
    else:
        print("LCA do not exist")
 
 
if __name__ == '__main__':
 
    """ Construct below tree
          1
        /   \
       /     \
      2          3
       \     / \
        4   5   6
           / \
          7   8
    """
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.right.right = Node(8)
 
    findLCA(root, root.right.left.left, root.right.right)
    findLCA(root, root.right.left.left, Node(10))
    findLCA(root, root.right.left.left, root.right.left.left)
    findLCA(root, root.right.left.left, root.right.left)
    findLCA(root, root.left, root.right.left)