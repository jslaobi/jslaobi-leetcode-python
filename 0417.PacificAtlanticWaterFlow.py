class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """时间复杂度: O(m * n)。
        空间复杂度: O(m * n)。
        """
        if not heights or not heights[0]:
            return []
        
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean_set):
            ocean_set.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in ocean_set and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean_set)
        
        # 因为我们从海岸去反推符合条件的区块, 所以我们从上下左右4个海岸调用4次dfs
        for r in range(rows):
            dfs(r, 0, pacific) #左
            dfs(r, cols - 1, atlantic) #右
        
        for c in range(cols):
            dfs(0, c, pacific) #上
            dfs(rows - 1, c, atlantic) #下

        result = []

        for r, c in (pacific & atlantic):
            result.append([r, c])
        
        return result