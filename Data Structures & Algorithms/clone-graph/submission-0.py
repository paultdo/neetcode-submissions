"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]
        
        self.visited[node] = Node(node.val)
        clone = self.visited[node]
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        
        return clone

