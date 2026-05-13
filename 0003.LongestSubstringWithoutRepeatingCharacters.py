class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
                