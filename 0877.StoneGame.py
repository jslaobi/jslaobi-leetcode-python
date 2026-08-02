class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """时间复杂度: O(n^2)。
        空间复杂度: O(n^2)。
        """
        n = len(piles)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                pick_left = piles[i] - dp[i+1][j]
                pick_right = piles[i] - dp[i][j-1]

                dp[i][j] = max(pick_left, pick_right)
        
        return dp[0][n-1] >= 0