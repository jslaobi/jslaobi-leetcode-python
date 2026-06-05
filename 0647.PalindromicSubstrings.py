class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        时间复杂度: O(n^2)，n 为字符串长度。
        空间复杂度: O(1)。
        """
        def expand_and_count(left: int, right: int) -> int:
            count = 0
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    count += 1
                else:
                    break
            return count
        
        total_count = 0
        for i in range(len(s)):
            total_count += expand_and_count(i,i)
            if i != len(s) - 1:
                total_count += expand_and_count(i,i + 1)
        
        return total_count