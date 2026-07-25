class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """时间复杂度: O(n^2)。
        空间复杂度: O(n)。
        """
        n = len(points)

        # Min-Heap - (wire_cost, point_index)
        min_heap = [(0, 0)]

        visited = set()
        total_cost = 0

        # 要遍历所有n个节点
        while len(visited) < n:
            cost, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue
            
            visited.add(curr)
            total_cost += cost

            curr_x, curr_y = points[curr]

            # 计算当前节点连接到所有其他不在visited里的节点的cost
            for next_point in range(n):
                if next_point not in visited:
                    next_x, next_y = points[next_point]
                    curr_cost = abs(next_x - curr_x) + abs(next_y - curr_y)

                    heapq.heappush(min_heap, (curr_cost, next_point))
            
        
        return total_cost
