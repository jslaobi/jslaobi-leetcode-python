class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """时间复杂度: O(n^2)。
        空间复杂度: O(n^2)。
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque()
        # queue里存放row,col,当前路径长度
        queue.append((0,0,1))
        # 将走过的格子标记为1,这样就不用额外的visited数组
        grid[0][0] = 1
        directions = [
            (-1,-1),(-1,0),(-1,1),
            (0,-1),         (0,1),
            (1,-1),(1,0),(1,1)  
        ]

        while queue:
            row, col, dist = queue.popleft()
            if row == n-1 and col == n-1:
                return dist
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr,nc,dist+1))
        
        return -1
