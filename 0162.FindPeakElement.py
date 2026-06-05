class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        时间复杂度: O(log n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # 如果nums[mid] < nums[mid + 1], mid肯定不会是peak,所以可以前进到mid+1
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
            # 反之也就是nums[mid] >= nums[mid + 1], mid+1肯定不会是peak,所以可以前进到mid
                right = mid
        
        return left