class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """时间复杂度: O(n * target)。
        空间复杂度: O(target)。
        """
        total_sum = sum(nums)

        # 如果是奇数,则不可能满足条件
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        # dp记录能否利用数字做成这个总和
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # 从目标到num倒序遍历
            for i in range(target, num - 1, - 1):
                # 能否减去这个数字,做成这个和
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
