class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        时间复杂度: O(n)，n 为字符串长度。
        空间复杂度: O(n)。
        """
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            window = s[i:i+10]
            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)
        
        return list(repeated)