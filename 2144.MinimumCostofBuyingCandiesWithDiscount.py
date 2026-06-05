class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        时间复杂度: O(n log n)，n 为糖果数量。
        空间复杂度: O(1)。
        """
        cost.sort(reverse=True)
        total = 0

        for i in range(len(cost)):
            if i % 3 != 2:
                total += cost[i]
        
        return total