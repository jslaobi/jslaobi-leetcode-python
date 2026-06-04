class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                row[c] = row[c] + row[c-1]
                
        result = row[-1]

        return result
        # memo = [[0] * n for _ in range(m)]

        # for r in range(m):
        #     memo[r][0] = 1

        # for c in range(n):
        #     memo[0][c] = 1

        # for r in range(1,m):
        #     for c in range(1,n):
        #         memo[r][c] = memo[r-1][c] + memo[r][c-1]
        
        # return memo[-1][-1]



        
        