class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """在旋转排序数组中查找目标值。

        时间复杂度: O(log n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            # 如果左半边是顺序
            if nums[left] <= nums[mid]:
                # 判断target在哪一个半边
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 否则,右半边是顺序
            else:
                # 判断target在哪一个半边
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1