class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for i in range(m + 1)]

        dp[0][0] = True

        # 处理dp[0], 也就是字符串s为空的情况
        for j in range(1, n+1):
            # 对于a*这种情况, *可以匹配0个或者很多个a. 我们先处理0个a的情况. 如果是a*,我们可以把a*整个消除掉,依照dp[0][j - 2]的值去设置dp[0][j]的值
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 如果s和p的对应字符相等, 或者p当前的字符是个'.'
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j - 1] == '*':
                    # 两种情况, 第一是a*对应0个a
                    char_match = dp[i][j] = dp[i][j-2]

                    # 否则,检查a*对应多个a的情况
                    if not char_match:
                        prev_char = p[j - 2]
                        # 因为我们构建了一个dp, 所以当有多个的情况比如aaaa, “”, “a”, “aa”, “aaa”这些情况会依次跟
                        # "a*"比较并设置为True, 所以这里我们只需要上一列dp[i - 1][j]的值
                        if prev_char == s[i - 1] or prev_char == '.':
                            dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]

