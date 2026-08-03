import math

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        n = len(stoneValue)
        dp = [-math.inf] * n

        # 从后往前推, 从最后一个石头开始, 倒推到起始石头数
        for i in range(n-1, -1, -1):
            take_sum = 0

            # 可以拿1-3块石头
            for j in range(3):
                if i + j < n:
                    take_sum += stoneValue[i + j]
                    # 当前分数 = 拥有的石头 - 对手能获得的最好成绩. 如果对手拿取的石头越界则分数是0
                    opponent_score = 0
                    if i + j + 1 < n:
                        opponent_score = dp[i + j + 1]
                        
                    dp[i] = max(dp[i], take_sum - opponent_score)
        
        # 由于是从后往前推的, dp[0]就是游戏开始时能取得的最好成绩
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


