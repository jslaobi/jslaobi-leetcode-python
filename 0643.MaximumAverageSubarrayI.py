class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 先用前k个元素(0 : k-1)的和作为current_sum和max_sum的初始值
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # 不断添加一个新数字并移除最老的一个数字
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k