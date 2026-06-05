class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(n)。
        """
        seen = set()

        for num in nums:
            if not num in seen:
                seen.add(num)
            else:
                return True

        return False 