class Node: 
    def __init__(self, data): 
        self.val = data
        self.left = None
        self.right = None
 
def boundaryOfBinaryTree(root):
    if not root:
        return
 
    left_boundary = []
    right_boundary = []
    leaves = []
    helper(root, 0, left_boundary, right_boundary, leaves)
    return left_boundary + leaves + right_boundary[::-1]
 
def helper(root, flag, left_boundary, right_boundary, leaves):
    if not root:
        return
 
    if not root.left and not root.right:
        leaves.append(root.val)
        return
 
    if flag == 0:
        left_boundary.append(root.val)
        helper(root.left, 1, left_boundary, right_boundary, leaves)
        helper(root.right, 2, left_boundary, right_boundary, leaves)
    elif flag == 1:
        left_boundary.append(root.val)
        if root.left:
            helper(root.left, 1, left_boundary, right_boundary, leaves)
            helper(root.right, 3, left_boundary, right_boundary, leaves)
        else:
            helper(root.right, 1, left_boundary, right_boundary, leaves)
    elif flag == 2:
        right_boundary.append(root.val)
        if root.right:
            helper(root.left, 3, left_boundary, right_boundary, leaves)
            helper(root.right, 2, left_boundary, right_boundary, leaves)
        else:
            helper(root.left, 2, left_boundary, right_boundary, leaves)
    else:
        helper(root.left, 3, left_boundary, right_boundary, leaves)
        helper(root.right, 3, left_boundary, right_boundary, leaves)
 
# Driver program to test above function 
root = Node(20)
root.left = Node(8) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
root.right = Node(22) 
root.right.right = Node(25)
print(boundaryOfBinaryTree(root))