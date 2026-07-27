class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        max1 = 0
        max2 = 0

        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        
        # 题目要求,需要-1
        return (max1 - 1) * (max2 - 1)