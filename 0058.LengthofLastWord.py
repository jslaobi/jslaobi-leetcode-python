class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        result = 0
        # 从后往前遍历
        i = len(s) - 1

        # 寻找最后一个单词
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # 计算最后一个单词长度
        while i >= 0 and s[i] != ' ':
            result += 1
            i -= 1
        
        return result