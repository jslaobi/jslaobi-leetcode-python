from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_count = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        rounds = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # 加入fresh_count > 0检查,防止过度数轮次
        while queue and fresh_count > 0:
            rounds += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh_count -= 1
        
        return rounds if fresh_count == 0 else -1
