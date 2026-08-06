class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """时间复杂度: O(m * n)。
        空间复杂度: O(m * n)。
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # base case: s1和s2都是空数组, 可以组成空数组s3
        dp[0][0] = True

        # 填充第一列, s2为空, 匹配s1到s3
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # 填充第一行, s1为空, 匹配s2到s3
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # s3在index (i + j - 1)
                
                # 检查如果当前字符从s1获取
                take_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                
                # 检查如果当前字符从s2获取
                take_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                
                # 检查以上两种情况能否成功
                dp[i][j] = take_s1 or take_s2
                
        return dp[m][n]

