class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        # 快慢指针
        left = 0
        right = 0
        
        for num in nums:
            if num != val:
                nums[left] = nums[right]
                left += 1

            right += 1
        
        return left