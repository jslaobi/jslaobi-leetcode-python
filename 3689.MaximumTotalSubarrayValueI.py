class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        # 根据题目描述以及示例2, 你可以多次选择同一个子数组. 所以这道题就是单纯的选出最大值和最小值, 并且乘以k
        max_value = max(nums)
        min_value = min(nums)

        return (max_value - min_value) * k