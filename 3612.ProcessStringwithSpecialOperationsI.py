class Solution:
    def processStr(self, s: str) -> str:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        # 如果直接操作字符串, 则python每次都会创建新的字符串会占用大量内存,所以一般选择操作数组,最后用"".join()转化成字符串
        result = []

        for char in s:
            if char == '*':
                if result:
                    result.pop()
            elif char == '#':
                result += result
            elif char == '%':
                result.reverse()
            else:
                result.append(char)
        
        return "".join(result)