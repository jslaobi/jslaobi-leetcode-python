class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        n = len(nums)
        result = [0] * n
        pos_index = 0
        neg_index = 1
        # 正数在奇数index, 负数在偶数index
        for i in range(n):
            if nums[i] > 0:
                result[pos_index] = nums[i]
                pos_index += 2
            else:
                result[neg_index] = nums[i]
                neg_index += 2
        
        return result