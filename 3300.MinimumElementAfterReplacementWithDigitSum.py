class Solution:
    def minElement(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n * d)，n 为数组长度，d 为数字位数。
        空间复杂度: O(1)。
        """
        min_sum = float('inf')

        for num in nums:
            current_sum = 0
            while num > 0:
                current_sum += num % 10
                num = num // 10
            min_sum = min(min_sum, current_sum)
        
        return min_sum