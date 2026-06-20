class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return False

            count[char] -= 1
        
        return True