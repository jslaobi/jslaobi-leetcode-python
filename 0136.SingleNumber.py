class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        result = 0

        for num in nums:
            result ^= num
        
        return result