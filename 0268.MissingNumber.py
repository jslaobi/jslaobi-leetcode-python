class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        n = len(nums)
        # 0...n的求和公式n * (n+1) // 2
        expected_sum = n * (n+1) // 2

        actual_sum = sum(nums)

        return expected_sum - actual_sum