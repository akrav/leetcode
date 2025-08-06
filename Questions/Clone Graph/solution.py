"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        self.dic = {}

        def dfs_create(node):
            if node is None:
                return None
            
            if node not in self.dic.keys():
                clone_node = Node(node.val)
                self.dic[node] = clone_node
            
            for neighbor in node.neighbors:
                if neighbor in self.dic.keys():
                    self.dic[node].neighbors.append(self.dic[neighbor])
                else:
                    self.dic[node].neighbors.append(dfs_create(neighbor))
            
            return self.dic[node]

        dfs_create(node)
        return self.dic[node]