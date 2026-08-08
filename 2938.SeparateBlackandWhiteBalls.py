class Solution:
    def minimumSteps(self, s: str) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        total_swaps = 0
        ones_count = 0

        for char in s:
            # 如果是1, 增加ones_count
            if char == '1':
                ones_count += 1
                
            # 如果是0, 则需要越过当前的所有1,移动到左边
            else:
                total_swaps += ones_count
        
        return total_swaps