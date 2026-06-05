class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        时间复杂度: O(log n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid
        
        return nums[left]