"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """时间复杂度: O(V + E)。
        空间复杂度: O(V)。
        """
        if not node:
            return None
        
        # 防止成环, visited的key是原node,value是clone后的node. 每次检查是否应该在visited里, 如果已经在,返回value里的node
        visited = {}

        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            clone = Node(curr_node.val)

            visited[curr_node] = clone

            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)