class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """时间复杂度: O(target * n)。
        空间复杂度: O(target)。
        """
        dp = [0] * (target + 1)

        # 有一种方式达成sum 0: 空集合
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]