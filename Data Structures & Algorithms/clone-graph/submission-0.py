"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mapping = {} 
        if not node:
            return None
        
        def dfs(node): #supposed to return the node in the mapping. everytime it traverses the new node, it has to ensure that everything already exists. 
            if node in mapping:
                return mapping[node]

        
            copy = Node(node.val)
            mapping[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy 

            

        return dfs(node)