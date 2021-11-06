# Algo:
# We first traverse through each and every of the nodes(of the graph) given to us, and then from that
# we have neighbours from which we make recursive call, to avoid looping we maintain a hashtable, so that everytime
# when we start working on a node, we check whether that node is already visited or not.

# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited={}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
    
        if node in self.visited:
            return self.visited[node]
        
        new_node =  Node(node.val, [])
        self.visited[node]=new_node
        
        if node.neighbors:
            new_node.neighbors= [self.cloneGraph(i) for i in node.neighbors]
        
        return new_node
        