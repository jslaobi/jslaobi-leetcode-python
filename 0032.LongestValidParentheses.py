class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(n)。
        """
        # 一开始放一个dummy值, 这样就可以判断:如果stack不是空,说明括号反而是匹配的. 如果stack为空,则出现了不匹配现象
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            # 如果是')'
            else:
                stack.pop()

                if not stack:
                    # 正如上面所说, 如果为空则出现了不匹配. 我们把-1给pop了,要把i添加进去
                    stack.append(i)
                # 如果不为空则为匹配,利用stack最上面的i计算最大长度
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length