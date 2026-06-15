import math
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        start = 0
        end = -1

        # 从前往后找右边界
        max_seen = -math.inf
        for i in range(n):
            # 如果比左边小的数, 就说明不是降序排列的
            if nums[i] < max_seen:
                end = i
            else:
                max_seen = nums[i]
        
        # 从后往前找左边界
        min_seen = math.inf
        for i in range(n-1, -1, -1):
            # 如果比右边大的数, 就说明不是降序排列的
            if nums[i] > min_seen:
                start = i
            else:
                min_seen = nums[i]
        
        return end - start + 1