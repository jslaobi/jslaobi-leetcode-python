"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        visited = {}

        def dfs(node):
            if not node:
                return None
            
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            
            clone.next = dfs(node.next)
            clone.random = dfs(node.random)

            return clone
        
        return dfs(head)