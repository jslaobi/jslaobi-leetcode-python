class Solution:
    def findMin(self, nums: List[int]) -> int:
        """在旋转排序数组中查找最小值。

        时间复杂度: O(n) 最坏情况，平均 O(log n)。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]