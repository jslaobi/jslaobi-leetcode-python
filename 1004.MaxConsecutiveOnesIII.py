class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        left = 0
        right = 0
        max_length = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
        
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                
                left += 1
            
            curr_length = right - left + 1
            max_length = max(max_length, curr_length)

            right += 1
        
        return max_length
            




