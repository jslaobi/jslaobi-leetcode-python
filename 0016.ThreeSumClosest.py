import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = -math.inf

        # 从0开始将i依次向前移动, 位置关系为i,left,right. i始终比移动的两个指针left和right更小
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum
                
                if abs(curr_sum - target) < abs(result - target):
                    result = curr_sum
                
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
            
        return result

