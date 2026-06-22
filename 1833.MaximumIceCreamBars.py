class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        # 按照消耗费用进行分类
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
        
        count = 0
        total = 0

        # 按照价格遍历freq(没有价格为0的冰激凌)
        for curr_price in range(1, max_cost + 1):
            # 如果当前价格没有冰激凌数,跳过
            if freq[curr_price] == 0:
                continue
            min_amount = min(freq[curr_price], (coins - total) // curr_price)
            count += min_amount
            total += min_amount * curr_price

            if total >= coins:
                break
        
        return count

        # costs.sort()
        # curr_sum = 0
        # count = 0
        # for cost in costs:
        #     if curr_sum + cost <= coins:
        #         curr_sum += cost
        #         count += 1
        
        # return count