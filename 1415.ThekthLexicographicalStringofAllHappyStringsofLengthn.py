class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        时间复杂度: O(2^n)，
        空间复杂度: O(n)。
        """
        result = []

        def backtrack(path):
            # 如果已经找到了k个, 则提前返回
            if len(result) == k:
                return

            # 如果找到了一个符合条件的字符串,则加入结果
            if len(path) == n:
                result.append(path[:])
                return

            for char in ['a', 'b', 'c']:
                if not path or char != path[-1]:
                    path.append(char)
                    backtrack(path)
                    path.pop()
        
        backtrack([])

        if len(result) == k:
            return "".join(result[-1])
        else:
            return ""