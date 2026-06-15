class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                total_count = max(total_count, current_count)
            else:
                current_count = 0
        
        return total_count