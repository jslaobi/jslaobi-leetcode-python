class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
            
            left += 1
            right -= 1
        
        return True