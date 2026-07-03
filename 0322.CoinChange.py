import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        时间复杂度: O(n^2)。
        空间复杂度: O(1)。
        """
        dp = [math.inf] * (amount + 1)

        # 使用0个硬币就可以达成数量0
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                # 尝试使用当前硬币获取最小值, dp[i - coin] + 1: 在coin值前的dp值, 加上当前这一枚硬币, 就是使用当前硬币的最小值
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                
        if dp[amount] == math.inf:
            return -1

        return dp[amount]