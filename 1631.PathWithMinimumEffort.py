import heapq
import math

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """时间复杂度: O(m*n log(m*n))。
        空间复杂度: O(m*n)。
        """
        rows = len(heights)
        cols = len(heights[0])

        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        min_efforts = [[math.inf] * cols for _ in range(rows)]
        min_efforts[0][0] = 0

        # Min-Heap: (max_effort_so_far, row, col)
        min_heap = [(0,0,0)]

        while min_heap:
            effort, row, col = heapq.heappop(min_heap)

            if row == rows - 1 and col == cols - 1:
                return effort
            
            # 如果当前的花费更大, 一定不是最优解, 不应该继续往前探索了
            if effort > min_efforts[row][col]:
                continue
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    step_effort = abs(heights[nr][nc] - heights[row][col])
                    new_max_effort = max(effort, step_effort)

                    if new_max_effort < min_efforts[nr][nc]:
                        min_efforts[nr][nc] = new_max_effort
                        heapq.heappush(min_heap, (new_max_effort, nr, nc))

        