from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """时间复杂度: O(1)。
        空间复杂度: O(1)。
        """
        # 使用3个set的集合保存已经见到的数
        rows = defaultdict(set)
        cols = defaultdict(set)
        # key: (r // 3, c // 3)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                if val in rows[r] or val in cols[c] or val in squares[(r//3,c//3)]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3,c//3)].add(val)
        
        return True