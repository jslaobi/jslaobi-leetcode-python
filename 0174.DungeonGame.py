class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        时间复杂度: O(m * n)，m 和 n 为网格的行列数。
        空间复杂度: O(m * n)。
        """
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 从迷宫尾部向前移动, 从右和下找到较小的需要生命值
                min_health = min(dp[i][j+1], dp[i+1][j])
                # 用最小需要生命值减去被扣除的生命,得到当前最小的能通过终点的生命值
                # 但是不能欠着生命值, 所以当前最小需要生命值为1
                dp[i][j] = max(1, min_health - dungeon[i][j])
        
        return dp[0][0]