from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """时间复杂度: O(n + m)。
        空间复杂度: O(n)。
        """
        counts = Counter()
        for i in basket1:
            counts[i] += 1
        for i in basket2:
            counts[i] -= 1

        swaps = []

        for value, count in counts.items():
            # 如果任何的count差值不为偶数, 则无法通过交换来达成相同的篮子
            # 注意题目要求是的the same baskets, 而不是两个篮子的cost相同
            if count % 2 != 0:
                return -1
            
            # 如果count = 4, 4个水果我们要移动2个, 也就是4 // 2
            transfer_needed = abs(count) // 2
            for i in range(transfer_needed):
                swaps.append(value)
            
        # 找到最便宜的水果
        global_min = min(min(basket1), min(basket2))
        # 将swaps排序
        swaps.sort()

        result = 0
        # 每次交换两个水果, 所以只需要交换前半部分
        swaps_needed = len(swaps) // 2

        for i in range(swaps_needed):
            # 每次交换我们都有两个选项
            # 1. 直接交换,费用为两个水果中较低的. 因为我们只遍历swaps前半部分,所以swaps[i]就是那个较低的费用
            # 2. 使用两次global_min, 比如global_min在basket2, 我们先用global_min跟basket1里的水果交换,然后再跟basket2里的交换. 通过使用global_min做桥, 达成间接交换
            result += min(swaps[i], global_min * 2)
        
        return result

