class UnionFind:
    def __init__(self, n):
        # 示例 {1: 1, 2: 2, 3: 3}
        self.parent = {i: i for i in range(1, n+1)}
        # 示例 {1: 0, 2: 0, 3: 0}
        self.rank = {i: 0 for i in range(1, n+1)}
        self.count = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        # 如果两个节点的根节点相同，说明它们已经在同一个集合中，返回False避免形成环路
        if root_i == root_j:
            return False
        
        # 将rank较小的根节点连接到rank较大的根节点上
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        
        self.count -= 1
        return True


class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        uf = UnionFind(n)

        # 按照cost从小到大排序
        connections.sort(key=lambda x: x[2])

        total_cost = 0

        for u, v, cost in connections:
            if uf.union(u, v):
                total_cost += cost
        
        # uf.count最多可以是1, 因为5个城市可以有4个连接(首尾可以不连, 不形成环路)
        # 如果uf.count大于1, 说明有些城市无法连接, 返回-1
        if uf.count > 1:
            return -1
        return total_cost
