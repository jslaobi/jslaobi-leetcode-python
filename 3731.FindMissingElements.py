class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """时间复杂度: O(k)。
        空间复杂度: O(k)。
        """
        min_val = min(nums)
        max_val = max(nums)

        nums_set = set(nums)

        result = []

        for num in range(min_val, max_val+1):
            if num not in nums_set:
                result.append(num)
        
        return result