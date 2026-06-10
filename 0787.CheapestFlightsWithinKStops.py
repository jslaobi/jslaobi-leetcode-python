import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        # 一共要跳k次
        for _ in range(k + 1):
            # 这里要复制一下prices数组,因为不想使用最新一轮起点更新后的价格. 比如1到2的价格在本轮从200更新成100, 我们不想拿起点价格100来计算,因为这样就导致偷加了一轮
            temp_prices = prices[:]

            for source, dest, price in flights:
                # 如果起点是inf,证明我们还没到达这里,跳过
                if prices[source] == math.inf:
                    continue
                # 但是终点还是要用temp_prices, 因为循环中如果发现了其他更好的终点价格,我们还是要使用那个价格做比较. 终点价格的更新不会导致偷加轮次
                if prices[source] + price < temp_prices[dest]:
                    temp_prices[dest] = prices[source] + price
            
            prices = temp_prices
        
        if prices[dst] == math.inf:
            return -1

        return prices[dst]