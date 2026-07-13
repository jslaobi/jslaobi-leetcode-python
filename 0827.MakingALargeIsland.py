class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """时间复杂度: O(n^2)。
        空间复杂度: O(n^2)。
        """
        n = len(grid)
        island_sizes = {}
        # 0是海水,1是陆地, 我们从2开始记录小岛id,这样可以避免使用一个2d数组visited
        island_id = 2

        def dfs(row, col, id):
            if row < 0 or row >= n or col < 0 or col >= n or grid[row][col] != 1:
                return 0
            
            grid[row][col] = id
            return 1+ dfs(row+1,col,id) + dfs(row-1,col,id) + dfs(row,col+1,id) + dfs(row,col-1,id)
        
        # 1. 找到所有小岛, 标记id, 记录面积
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island_sizes[island_id] = dfs(row, col, island_id)
                    island_id += 1
        
        result = 0
        # 用于检查是否全是1的情况
        has_zero = False

        # 2. 尝试把0变成1, 然后检查4周是否与小岛相连
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    has_zero = True
                    seen_islands = set()

                    directions = [(-1,0),(1,0),(0,-1),(0,1)]

                    # 检查四周是否有陆地
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if 0<=nr<n and 0<=nc<n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])
                    
                    # 0变1那个格子本身
                    curr_size = 1
                    for i in seen_islands:
                        curr_size += island_sizes[i]
                    result = max(result, curr_size)

        
        if has_zero:
            return result
        else:
            return n * n

