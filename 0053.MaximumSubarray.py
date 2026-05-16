class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 不能设为0, 因为可能是[-1]这种情况
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(current_sum, max_sum)
            # 如果和是负数,那么从这里起以负数相加一定小于以0相加,所以舍弃到并从零开始
            if current_sum < 0:
                current_sum = 0
            
        return max_sum

