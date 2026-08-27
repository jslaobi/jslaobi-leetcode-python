class Solution:
    def totalNQueens(self, n: int) -> int:
        """时间复杂度: O(n!)。
        空间复杂度: O(n)。
        """
        cols = set()
        pos_diag = set()
        neg_diag = set()
        self.count = 0

        def dfs(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                dfs(r+1)
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
        
        dfs(0)
        return self.count
