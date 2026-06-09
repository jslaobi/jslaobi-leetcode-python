class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 转换成set以获得O(1)的搜索速度
        nums_set = set(nums)
        max_streak = 0

        for num in nums_set:
            # 当找到一个num-1不存在set里的数,则找到了一个新的连续数的开始
            if (num - 1) not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                max_streak = max(max_streak, current_streak)
        
        return max_streak