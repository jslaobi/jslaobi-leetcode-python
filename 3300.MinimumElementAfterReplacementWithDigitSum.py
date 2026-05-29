class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')

        for num in nums:
            current_sum = 0
            while num > 0:
                current_sum += num % 10
                num = num // 10
            min_sum = min(min_sum, current_sum)
        
        return min_sum