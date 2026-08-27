class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[i]:
                return False

            temp = board[row][col]
            board[row][col] = '#'

            found = dfs(row-1, col, i+1) or  dfs(row+1, col, i+1) or dfs(row, col-1, i+1) or dfs(row, col+1, i+1)
            board[row][col] = temp
            return found
        # 先找到一个首字母相符的格子开始    
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False
