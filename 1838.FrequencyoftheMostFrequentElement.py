class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = 0
        window_sum = 0
        max_freq = 0

        while right < len(nums):
            # 扩展窗口
            window_sum += nums[right]

            # 如果窗口内超额, 则需要缩小窗口
            while nums[right] * (right - left + 1) - window_sum > k:
                # 先减后移动left
                window_sum -= nums[left]
                left += 1
            
            max_freq = max(max_freq, right - left + 1)
            right += 1
            
        return max_freq
        