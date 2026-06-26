class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        counts = {}
        max_length = 0
        max_freq = 0
        left = 0
        right = 0
        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(counts.values())

            # 检查条件: 窗口总长度 - 当前最多字符(正在重复的字符) = 不符合条件的字符
            # 如果不符合条件的字符 > k, 就不能通过替换k个字符来完成统一字符, 需要从左边弹出字符
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                # 重新获取新的max_freq
                max_freq = max(counts.values())

            max_length = max(max_length, right - left + 1)
            right += 1
            
        return max_length