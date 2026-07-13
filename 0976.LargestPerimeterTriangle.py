class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(1)。
        """
        nums.sort(reverse=True)

        # 数组是降序排列, 所以前面的数更大
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i+1] + nums[i+2] + nums[i]
        
        return 0