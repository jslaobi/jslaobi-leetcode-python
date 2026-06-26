from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        counts = Counter(nums)

        for num, count in counts.items():
            if count == 1:
                return num