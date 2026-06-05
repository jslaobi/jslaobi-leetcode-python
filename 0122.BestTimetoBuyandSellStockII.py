class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        时间复杂度: O(n)，n 为价格长度。
        空间复杂度: O(1)。
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        
        return max_profit