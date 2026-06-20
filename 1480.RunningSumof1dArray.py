class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        return nums