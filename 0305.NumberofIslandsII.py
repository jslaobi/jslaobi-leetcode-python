class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        island_count = 0
        parent = {}
        result = []

        def find(node: tuple[int, int]) -> tuple[int, int]:
            # 压缩路径, 直接将节点指向根
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
    
        def union(node1: tuple[int, int], node2: tuple[int, int]):
            nonlocal island_count
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                parent[root1] = root2
                island_count -= 1
        
        for r,c in positions:
            node = (r, c)

            # 题目有可能给我们重复的坐标
            if node in parent:
                result.append(island_count)
                continue

            # 第一步, 添加一个新的小岛
            parent[node] = node
            island_count += 1

            # 第二步, 检查能否与4个方向的相邻节点合并
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                neighbor = (nr, nc)

                # 先检查不越界, 然后如果四周坐标有在parent里的,则说明可以合并
                if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                    union(node, neighbor)
            
            result.append(island_count)
        
        return result
