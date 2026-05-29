class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >=len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        
        return result