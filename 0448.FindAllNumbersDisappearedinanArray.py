class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        num_set = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in num_set:
                result.append(i)
        
        return result