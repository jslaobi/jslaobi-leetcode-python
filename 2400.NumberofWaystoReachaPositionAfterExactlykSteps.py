from functools import cache

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        """时间复杂度: O(k^2)。
        空间复杂度: O(k^2)。
        """
        MOD = 10**9 + 7

        @cache
        def dp(curr_position, remaining_steps):
            if remaining_steps == 0:
                if curr_position == endPos:
                    return 1
                else:
                    return 0
            
            ways_left = dp(curr_position - 1, remaining_steps - 1)
            ways_right = dp(curr_position + 1, remaining_steps - 1)

            return (ways_left + ways_right) % MOD
        
        return dp(startPos, k)
