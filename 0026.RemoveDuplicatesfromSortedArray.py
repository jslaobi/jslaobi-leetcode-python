class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                # 当找到一个新数字,向前移动一位并存储新数字
                slow += 1
                nums[slow] = nums[fast]
                 
        return slow + 1