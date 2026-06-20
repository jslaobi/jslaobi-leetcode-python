class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        result = 0
        curr_height = 0

        for height in gain:
            curr_height += height
            result = max(result, curr_height)
        
        return result