class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        时间复杂度: O(n)，n 为字符串长度。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True