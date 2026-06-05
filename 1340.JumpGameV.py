class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """
        时间复杂度: O(n * d)，n 为数组长度，d 为最大跳跃距离。
        空间复杂度: O(n)。
        """
        n = len(arr)
        memo = [0] * n

        def dfs(i):
            if memo[i] != 0:
                return memo[i]

            # 按照题目例子2,一步都不跳算作1
            max_path = 1

            # 向右跳的情况
            for x in range(1, d + 1):
                j = i + x

                if j >= n or arr[i] <= arr[j]:
                    break
                
                max_path = max(max_path, 1 + dfs(j))

            # 向左跳的情况
            for x in range(1, d + 1):
                j = i - x

                if j < 0 or arr[i] <= arr[j]:
                    break
                
                max_path = max(max_path, 1 + dfs(j))
            
            # 记住从当前能跳跃的最多步数
            memo[i] = max_path
            return max_path
        
        result = max(dfs(i) for i in range(n))

        return result