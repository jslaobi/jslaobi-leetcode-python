from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
            时间复杂度: O(n)。
            空间复杂度: O(1)。
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                
                left += 1