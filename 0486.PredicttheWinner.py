class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        """时间复杂度: O(n^2)。
        空间复杂度: O(n^2)。
        """
        n = len(nums)

        # 建立2d数组dp
        dp = [[0] * n for _ in range(n)]

        # 先填充斜对角. 也就是[1][1],[2][2]这种对应只剩一个数字的情况(长度为1时), 只能选取那个剩下的数字
        for i in range(n):
            dp[i][i] = nums[i]
        
        # 再填充长度为2-n时的情况
        for length in range(2, n+1):
            # 因为要保证子数组是length的长度, 所以最右边只能到n - length + 1, 再往右就能不能保证length长度或者越界
            # 比如n = 5, length = 3, 5 - 3 + 1 = 3. 在range(3)就要停止循环,也就是i = 0,1,2
            for i in range(n - length + 1):
                # j则要始终跟i保持length的距离,所以j = i + length - 1
                j = i + length - 1
                
                # 当前可以选择左边或者右边. dp的length一定比当前nums[i]小1, dp[i+1][j]比nums[i]少了左边的数, dp[i][j-1]比nums[i]少了左边的数
                # 因为是由length由小到大计算的, 所以当计算到nums[i]时, 可以保证dp[i+1][j]和dp[i][j-1]已经计算过了
                take_left = nums[i] - dp[i+1][j]
                take_right = nums[j] - dp[i][j-1]

                dp[i][j] = max(take_left, take_right)

        # i-起始点, j-终止点. 所以dp[0][n-1]得到的是整个数组的得分正负情况
        return dp[0][n-1] >= 0 