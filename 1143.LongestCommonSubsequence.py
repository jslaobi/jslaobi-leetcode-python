class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """时间复杂度: O(m*n)。
        空间复杂度: O(m*n)。
        """
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # 如果字符相等, 用dp[i-1][j-1]的值加1(dp[0][0] = 0, 循环从1到m或n)
                # 注意这里比较的是i-1和j-1
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                # 如果不相等, 取上方或者左边的较大值
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]