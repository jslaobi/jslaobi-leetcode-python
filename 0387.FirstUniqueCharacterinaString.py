from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        counts = Counter(s)

        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        
        return -1
        