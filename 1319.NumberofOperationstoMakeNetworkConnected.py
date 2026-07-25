class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """时间复杂度: O(E + V)。
        空间复杂度: O(V)。
        """
        # 如果connections数量不足, 直接返回-1
        if len(connections) < n - 1:
            return -1
        
        parent = [i for i in range(n)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]
        
        components = n

        for u, v in connections:
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parent[root_u] = root_v
                components -= 1
        
        return components - 1
