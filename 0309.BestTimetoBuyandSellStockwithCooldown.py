class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        memo = {}

        def dfs(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            
            # memo里记录当前天数+是否持有股票的组合的最大利润
            # 即使是同一天,是否持有股票应该当作两种情况处理, 所以memo里用的是(i, holding)
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            if holding:
                # 1. 如果选择卖出, 并且加上2天后的选择(因为i+1天cooldown无法交易)
                sell = prices[i] + dfs(i+2, False)
                # 如果选择持有, 则当前没有收益, 明天再做选择
                hold = dfs(i+1, True)

                memo[(i, holding)] = max(sell, hold)
            
            else:
                # 1. 今天买入, 利润为-prices[i], 再加上明天的选择
                buy = -prices[i] + dfs(i+1, True)
                # 2. 今天不买入, 明天再做选择
                hold = dfs(i+1, False)

                memo[(i, holding)] = max(buy, hold)
            

            return memo[(i, holding)]
        
        return dfs(0,False)
            
