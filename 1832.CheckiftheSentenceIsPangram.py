class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        char_set = set(sentence)
        return len(char_set) == 26