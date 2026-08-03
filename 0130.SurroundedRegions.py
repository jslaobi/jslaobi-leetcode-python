class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """时间复杂度: O(m * n)。
        空间复杂度: O(m * n)。
        """
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # 把从边缘能访问到的O标记成T, 剩下的所有的O都是符合条件的
            board[r][c] = 'T'

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        # 标注跟边缘相连的0, 首先是上下边
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        
        # 然后标记左右边
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        
        # 最后扫描一边, 将O标记为X, 将T标记回O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'