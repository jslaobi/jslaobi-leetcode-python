import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        #两条对角线上不能有棋子
        pos_diag = set()
        neg_diag = set()

        result = []
        # 棋盘是n*n
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                # 添加结果时, 要把每一行先转换为字符串
                current_solution = ["".join(row) for row in board]
                result.append(current_solution)
                return
            for c in range(n):
                # 如果直线或者两条对角线有棋子则跳过
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # 依然是backtrack三部曲,只不过每一步要处理3个set所以代码多一些
                # 1. 放置棋子
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # 2. 进行到下一行
                backtrack(r + 1)

                # 3. 收回棋子
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)

        return result

                
            