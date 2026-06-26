from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        counts = Counter(text)
        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])