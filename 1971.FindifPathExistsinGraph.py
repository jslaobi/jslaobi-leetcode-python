class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # parent = [0, 1, 2, ..., n-1]
        parent = list(range(n))
        # rank = [1, 1, 1, ..., 1]
        rank = [1] * n

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            
            return parent[i]
        
        def union(i: int, j: int):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                elif rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
        
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)
