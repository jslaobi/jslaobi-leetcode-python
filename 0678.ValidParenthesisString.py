class Solution:
    def checkValidString(self, s: str) -> bool:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        # 记录最大和最小左括号的数量
        min_open = 0
        max_open = 0

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else: # char == '*'
                min_open -= 1 # 用 '*' 充当 ')'
                max_open += 1 # 用 '*' 充当 '('

            # 即使充当了左括号,右括号仍然太多,则返回False
            if max_open < 0:
                return False
            
            # min_open不能为负数,需要最少是0. 以防止出现*(被认定为合法的情况
            min_open = max(min_open, 0)
        
        # 检查min_open是否为0, 如果min_open大于0, 则max_open更会大于0,导致所有可能都不成立
        return min_open == 0