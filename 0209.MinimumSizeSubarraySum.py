import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        result = math.inf
        curr_sum = 0
        left = 0
        right = 0

        # 滑动窗口
        while right < len(nums):
            curr_sum += nums[right]
            # 只要curr_sum大于target, 都是符合条件的
            while curr_sum >= target and left <= right:
                result = min(result, right - left + 1)

                curr_sum -= nums[left]
                left += 1
            
            right += 1

        if result == math.inf:
            result = 0
            
        return result