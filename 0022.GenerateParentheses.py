class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """回溯生成有效括号组合。

        时间复杂度: O(C_n)，Catalan 数量级，最坏情况约 O(4^n / n^{3/2})。
        空间复杂度: O(n)，递归栈深度和当前构建字符串长度。
        """
        result = []

        def backtrack(open_count, closed_count, current_string):
            if len(current_string) == n * 2:
                result.append(current_string)
                return
            
            if open_count < n:
                backtrack(open_count + 1, closed_count, current_string+"(")
            
            # 注意这里不能用elif，否则只会添加 (()) 这种情况
            if closed_count < open_count :
                backtrack(open_count, closed_count + 1, current_string+")")

        backtrack(0, 0, "")
        return result
