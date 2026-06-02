class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n 
        provinces = n

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            
            return parent[i]
        
        def union(u: int, v: int) -> bool:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False
            
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            
            return True
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        provinces -= 1
        
        return provinces
