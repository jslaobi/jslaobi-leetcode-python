class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """时间复杂度: O(log n)。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1