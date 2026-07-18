class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        """时间复杂度: O(k * log C * n)。
        空间复杂度: O(1)。
        """
        result = 0

        for machine in composition:
            left = 0
            right = 10 ** 9
            best_for_machine = 0

            # 随机选择一个合金数量
            while left <= right:
                mid = left + (right - left) //2
                curr_cost = 0
                # n是所有金属种类, 用j遍历, 计算当前机器生产mid个合金的cost
                for j in range(n):
                    required_metal = mid * machine[j]
                    # 如果库存不足, 则需要购买, 花费(required_metal - stock[j]) * cost[j]
                    if required_metal > stock[j]:
                        curr_cost += (required_metal - stock[j]) * cost[j]
                
                if curr_cost <= budget:
                    best_for_machine = mid
                    left = mid + 1
                else:
                    right = mid - 1
            

            result = max(result, best_for_machine)
        
        return result