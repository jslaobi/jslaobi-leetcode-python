class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        res = []
        
        for i in range(n):
            res.append(nums[i])     
            res.append(nums[i + n])  
            
        return res