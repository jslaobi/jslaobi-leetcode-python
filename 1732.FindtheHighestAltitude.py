class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        curr_height = 0

        for height in gain:
            curr_height += height
            result = max(result, curr_height)
        
        return result