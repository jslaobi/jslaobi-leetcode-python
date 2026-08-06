class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """时间复杂度: O(n + e)。
        空间复杂度: O(n)。
        """
        parent = list(range(n))
        size = [1] * n
        total = n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            # 如果root相同则说明是相连的
            if root1 == root2:
                return 0

            # 否则,则不相连,进行合并
            if size[root1] > size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]

            return 1

        for u, v in edges:
            # 题目求的是相连的数量, 用总数total减去不相连的就是答案
            total -= union(u, v)

        return total
        
