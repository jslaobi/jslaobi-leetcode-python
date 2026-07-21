class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        n = len(cost)
        prev1 = 0
        prev2 = 0

        for i in range(2, n+1):
            curr = min(cost[i-1]+prev1, cost[i-2]+prev2)

            prev2 = prev1
            prev1 = curr
            
        return prev1

        
        # n = len(cost)

        # dp = [0] * (n + 1)

        # for i in range(2, n+1):
        #     # 一步前和两步前的cost的较小值, cost[i-1]+dp[i-1]: 到达dp[i-1]这个格子的cost+离开这个格子需要的cost
        #     dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        
        # return dp[n]