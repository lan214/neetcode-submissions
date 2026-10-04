"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.copy = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node.val in self.copy:
            return self.copy[node.val]

        copyNode = Node(node.val)
        self.copy[node.val] = copyNode

        for neighbor in node.neighbors:
            copyNode.neighbors.append(self.cloneGraph(neighbor))
        
        return copyNode