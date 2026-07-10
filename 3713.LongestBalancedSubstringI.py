class Solution:
    def longestBalanced(self, s: str) -> int:
        """时间复杂度: O(n^2)。
        空间复杂度: O(1)。
        """
        n = len(s)
        max_len = 0

        for i in range(n):
            # 从每个i开始重置这些变量,j会逐渐向右越来越大
            counts = [0] * 26
            max_freq = 0
            unique_chars = 0

            for j in range(i, n):
                char_index = ord(s[j]) - ord('a')
                if counts[char_index] == 0:
                    unique_chars += 1
                
                counts[char_index] += 1

                max_freq = max(max_freq, counts[char_index])

                curr_length = j - i + 1
                # 如果最大的出现次数乘以字符数等于当前长度, 说明所有的字符都有相等的最大出现次数
                if max_freq * unique_chars == curr_length:
                    max_len = max(max_len, curr_length)
        
        return max_len