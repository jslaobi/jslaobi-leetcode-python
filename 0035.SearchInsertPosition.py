class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """在排序数组中搜索插入位置。

        时间复杂度: O(log n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        
        return left