class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        two_steps_before = 1
        one_step_before = 2

        for i in range(2, n):
            current = two_steps_before + one_step_before
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before
        # if n <= 2:
        #     return n
        
        # dp = [0] * n

        # dp[0] = 1
        # dp[1] = 2

        # for i in range(2, n):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        
        # return dp[n-1]
