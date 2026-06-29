class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 使用min_heap来保证如果遇到高的水位会推到底部,每步只处理当前最低的水位. 这样最先到达右下角(n - 1, n - 1)的就是最短时间
        min_heap = [(grid[0][0], 0, 0)]

        # 使用一个set来保证不会走回头路,只前进到新的格子
        visited = set((0,0))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while min_heap:
            curr_water_level, row, col = heapq.heappop(min_heap)

            # 如果到达了(n - 1, n - 1), 则找到了答案
            if row == n - 1 and col == n - 1:
                return curr_water_level
            
            # 处理4个方向
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    next_water_level = max(curr_water_level, grid[nr][nc])
                    heapq.heappush(min_heap, (next_water_level, nr, nc))
        
        return -1

