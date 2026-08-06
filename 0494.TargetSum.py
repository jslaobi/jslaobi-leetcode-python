class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """时间复杂度: O(n * total_sum)。
        空间复杂度: O(n * total_sum)。
        """
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0

        n = len(nums)

        offset = total_sum

        # 因为要容纳正负两种情况, 所以需要两倍宽度的dp(-total_sum to +total_sum)
        dp = [[0] * (2 * total_sum + 1) for _ in range(n)]

        # base case: 第一个数是+和-两种情况
        dp[0][nums[0] + offset] += 1
        dp[0][-nums[0] + offset] += 1

        for i in range(1, n):
            # 检查所有的可能的和
            for current_sum in range(-total_sum, total_sum + 1):
                
                # 如果在之前的数字有至少一个有效的和
                if dp[i-1][current_sum + offset] > 0:
                    
                    # 选项1: 加当前数字
                    dp[i][current_sum + nums[i] + offset] += dp[i-1][current_sum + offset]
                    
                    # 选项2: 减当前数字
                    dp[i][current_sum - nums[i] + offset] += dp[i-1][current_sum + offset]
                    
        # 返回使用n个元素所能组成的和的数量
        return dp[n-1][target + offset]