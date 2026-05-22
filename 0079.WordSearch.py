class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """DFS 查找单词是否存在于矩阵中。

        时间复杂度: O(m*n*4^L)，m*n 为矩阵大小，L 为单词长度。
        空间复杂度: O(L)，递归栈深度。
        """
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
                # 这里是dfs(i,j,0)而不是dfs(i,j,1)的原因是,虽然dfs会为0做一个重复检查
                # 但是我们仍然需要之后的把格子标记成#的步骤,所以为了不重复代码,这里传入0做重复检查是可接受的
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True

        return False
