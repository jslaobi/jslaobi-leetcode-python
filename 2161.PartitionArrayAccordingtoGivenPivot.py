class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1
        
        for i in range(n-1, -1, -1):
            if nums[i] > pivot:
                result[right] = nums[i]
                right -= 1 
        
        while left <= right:
            result[left] = pivot
            left += 1
        
        return result