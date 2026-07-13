class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """时间复杂度: O(amount * len(coins))。
        空间复杂度: O(amount)。
        """
        dp = [0] * (amount + 1)

        dp[0] = 1

        # 这道题求的是combination, combination - 不允许出现顺序变种,1+2和2+1被认为是同一个答案. permutation - 允许1+2和2+1两种情况
        # 外层循环是coin，强行规定了硬币的选择顺序（比如只能1->2->5），避免了产生 1+2 和 2+1 这种排列的区别，因此是combination。
        # 将内外层循环互换, 就能得到permutation
        for coin in coins:
            for i in range(coin, amount+1):
                # dp[i - coin]种方式+当前硬币=dp[i]
                dp[i] += dp[i - coin]
        
        return dp[amount]
