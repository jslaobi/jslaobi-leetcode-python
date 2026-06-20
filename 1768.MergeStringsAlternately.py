class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        i = 0
        j = 0
        result = []
        while i < len(word1) and j <len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        result.append(word1[i:])
        result.append(word2[j:])
        
        return "".join(result)