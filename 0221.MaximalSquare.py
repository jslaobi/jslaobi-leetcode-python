class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        时间复杂度: O(m * n)，m 和 n 为矩阵行列数。
        空间复杂度: O(m * n)。
        """
        if not matrix:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0
        for row in range(m):
            for col in range(n):
                # 当前的最大面积是由上面,左面和左上的最小者决定
                if matrix[row][col] == '1':
                    dp[row+1][col+1] = min(dp[row][col+1], dp[row+1][col], dp[row][col]) + 1
                    max_side = max(max_side, dp[row+1][col+1])
                # 否则就设为0, 但是因为初始化已经为0, 所以不需要写else: dp[row+1][col+1] = 0
        
        return max_side * max_side
                