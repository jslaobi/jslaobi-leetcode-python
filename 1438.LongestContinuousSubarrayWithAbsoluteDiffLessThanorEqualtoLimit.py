class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()
        left = 0
        max_length = 0
        # nums = [8, 2, 4, 7], left = 0 
        # 第一轮: right: 0, num: 8, max_dq: [8], min_dq: [8], max_dq[0] (8) - min_dq[0] (8) = 0, max_length = 1

        # 第二轮: right: 1, num: 2, max_dq = [8, 2], min_dq = [2], max_dq[0] (8) - min_dq[0] (2) = 6, 6 > 4, 大于窗口长度
        # 开始移动left, left在index=0, 也就是8. 8等于max_dq[0], 所以从max_dq中移除8. max_dq = [2], left移动到1

        # 第三轮: right: 2, num: 4. max_dq[-1] < 4, 所以max_dq中移除2, 添加4. max_dq = [4], min_dq = [2, 4]. max_dq[0] (4) - min_dq[0] (2) = 2, max_length = 2

        # 第四轮: right = 3, num = 7. max_dq[-1] < 7, 所以max_dq中移除4, 添加7. max_dq = [7], min_dq = [2, 4, 7], max_dq[0] (7) - min_dq[0] (2) = 5, 5 > 4, 大于窗口长度
        # 开始移动left, left在index=1, 也就是2. 2等于min_dq[0], 所以从min_dq中移除2. min_dq = [4, 7], left移动到2, max_length = 2

        # 最后输出为2

        # 使用max_dq和min_dq的原因是, 当我们移除了一个最大的值, 新的第一个元素就是新的最大值. 最小值也同理.
        # 比如一开始是[8], 然后是[8,2],然后是[8,4].当移除了8,下一个最大值就是[4]
        for right, num in enumerate(nums):
            while max_dq and max_dq[-1] < num:
                max_dq.pop()
            max_dq.append(num)

            while min_dq and min_dq[-1] > num:
                min_dq.pop()
            min_dq.append(num)

            while max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[left]:
                    max_dq.popleft()
                if min_dq[0] == nums[left]:
                    min_dq.popleft()
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length