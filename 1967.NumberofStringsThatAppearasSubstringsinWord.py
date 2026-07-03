class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        时间复杂度: O(n^2)。
        空间复杂度: O(1)。
        """
        count = 0

        for pattern in patterns:
            if pattern in word:
                count += 1
        
        return count