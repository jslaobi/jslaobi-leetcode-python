from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """时间复杂度: O(m * n * k)。
        空间复杂度: O(m * n)。
        """
        m = len(grid)
        n = len(grid[0])

        # Queue里存放的: (row, col, remaining_k, steps)
        queue = deque()
        queue.append((0, 0, k, 0))

        # visited hash map记录在(row, col)下, 所拥有的最多k
        

        visited = {(0, 0): k}

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r, c, curr_k, steps = queue.popleft()

            if r == m - 1 and c == n - 1:
                return steps
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < m and 0 <= nc < n:
                    # 0 (empty) or 1 (obstacle)
                    next_k = curr_k - grid[nr][nc]

                    # 如果next_k还有剩余, 同时这个格子没有被访问或者当前剩余k比原来存储的更大
                    if next_k >= 0 and visited.get((nr, nc), -1) < next_k:
                        visited[(nr, nc)] = next_k
                        queue.append((nr, nc, next_k, steps + 1))
        
        return -1