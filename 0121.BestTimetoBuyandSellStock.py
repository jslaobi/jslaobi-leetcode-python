class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # 如果找到更小的价格,则更新min_price
            if price < min_price:
                min_price = price
            # 否则就检查并计算最大利润
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit