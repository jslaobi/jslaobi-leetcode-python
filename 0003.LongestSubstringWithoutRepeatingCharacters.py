class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口查找无重复子串。

        时间复杂度: O(n)，n 为字符串长度。
        空间复杂度: O(min(n, m))，m 为字符集大小，最多使用哈希集合存储窗口内字符。
        """
        left = 0
        char_set = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                # 找到一个新的重复字符时，移动left，直到把这个旧的重复字符移出窗口
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
                