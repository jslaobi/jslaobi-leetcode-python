import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(n)。
        """
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)

        if min_val == max_val:
            return 0
        
        n = len(nums)

        bucket_size = math.ceil((max_val - min_val) / (n - 1))

        bucket_num = (max_val - min_val) // bucket_size + 1

        buckets = []

        for _ in range(bucket_num):
            buckets.append([float('inf'), float('-inf')])

        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        prev_max = min_val

        for i in range(bucket_num):
            if buckets[i][0] == float('inf'):
                continue
            
            max_gap = max(max_gap, (buckets[i][0] - prev_max))

            prev_max = buckets[i][1]
        
        return max_gap