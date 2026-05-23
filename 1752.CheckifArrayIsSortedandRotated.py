class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        length = len(nums)

        # 这里用%的原因是数组相当于一个环形,我们需要比较最后一位和第一位,%就能完美处理并且避免越界
        for i in range(length):
            if nums[i] > nums[(i + 1) % length]:
                drops += 1
        
        if drops > 1:
            return False
        
        return True