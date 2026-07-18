class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        # stack中价格升序
        stack = []

        for i, price in enumerate(prices):
            # 如果找到一个更低的价格, 就可以给之前的价格打折. 从stack中取之前的价格
            while stack and price <= prices[stack[-1]]:
                index = stack.pop()
                # 折扣的值为price(prices[j])
                result[index] -= price
            
            stack.append(i)
        
        return result