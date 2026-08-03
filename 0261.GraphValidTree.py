class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """时间复杂度: O(n + e)。
        空间复杂度: O(n)。
        """
        # 如果少于n-1, 则当前节点无法保证连接到其他所有节点. 如果大于n-1,则有环,不符合条件
        if len(edges) != n - 1:
            return False

        # 每个节点都是自己的parent
        parent = list(range(n))
        rank = [1] * n

        def find(node):
            if parent[node] == node:
                return node

            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            # 如果有相同的root,则证明有环
            if root1 == root2:
                return False

            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root1] = root2
                rank[root2] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True