class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        # len(triangle) - 2: 从倒数第二层开始
        # -1: 一直到最上面一层(因为range不包括当前数值,所以是-1而不是0)
        # -1: 倒序遍历
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 用当前值加上下面相邻两个值的最小值,便是当前最小值
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]