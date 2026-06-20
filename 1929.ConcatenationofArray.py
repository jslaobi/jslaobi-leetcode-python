class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        n = len(nums)
        ans = [0] * 2 * n

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans