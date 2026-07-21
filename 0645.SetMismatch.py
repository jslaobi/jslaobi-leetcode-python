class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))

        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum

        return [duplicate, missing]
