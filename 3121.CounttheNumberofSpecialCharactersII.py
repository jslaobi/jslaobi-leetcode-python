class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        时间复杂度: O(n)，n 为字符串长度。
        空间复杂度: O(1)。
        """
        states = [0] * 26
        # 0 - 初始状态
        # 1 - 发现一个小写字母
        # 2 - 发现一对特殊字符
        # -1 - 无效情况,例如大写字母后又出现小写字母等永远不可能达成特殊字符的情况
        for char in word:
            i = ord(char.lower()) - ord('a')

            if char.islower():
                if states[i] == 0:
                    states[i] = 1
                elif states[i] == 2:
                    states[i] = -1
            
            else:
                if states[i] == 0:
                    states[i] = -1
                elif states[i] == 1:
                    states[i] = 2

        return states.count(2)