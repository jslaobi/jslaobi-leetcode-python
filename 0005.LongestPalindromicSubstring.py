class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(length):
            # 处理奇数对称和偶数对称两种情况
            left1, right1 = expand(i, i)
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        # 因为s[start:end]是左闭右开区间，即包含start但不包含end，所以要end+1
        return s[start:end+1]