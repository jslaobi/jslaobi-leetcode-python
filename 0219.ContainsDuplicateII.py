class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(min(n, k))，k 为限制范围。
        """
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and (i - seen[num]) <= k:
                return True
            
            seen[num] = i
        
        return False