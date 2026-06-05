class Solution:
    def isNumber(self, s: str) -> bool:
        """
        时间复杂度: O(n)，n 为字符串长度。
        空间复杂度: O(1)。
        """
        seen_digit = False
        seen_exponent = False
        seen_dot = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            
            elif char in "+-":
                # +-只有可能出现在最开始,或者eE的后面,如3e+7
                if i > 0 and s[i - 1] not in "eE":
                    return False
            
            elif char in "eE":
                # 只能有一个eE,并且在之前要出现过数字
                # e3这种的就为无效,因为e之前没有数字
                # 这里不能写or not s[i-1].isdigit(),因为4.e3这种也被leetcode当作有效
                if seen_exponent or not seen_digit:
                    return False
                
                seen_exponent = True
                # 这里保证了e后面要有数字,2e这种就会在后面认定为无效
                seen_digit = False
            
            elif char == '.':
                # 只能有一个. 而且.不能出现在e在后面,比如99e2.5为无效
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            
            else:
                return False
        # 避免了之前说的2e这种情况
        return seen_digit