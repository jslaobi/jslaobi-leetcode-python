class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                
            if candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate