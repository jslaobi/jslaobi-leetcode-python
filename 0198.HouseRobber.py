class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_money = 0
        rob1, rob2 = 0, 0

        # rob1 - 两步之前
        # rob2 - 一步之前
        # max_money - 当前步数
        for num in nums:
            max_money = max(rob2, rob1 + num)
            # 每次向前移动时,将两步之前更新为一步之前的值,一步之前更新为当前的值
            rob1 = rob2
            rob2 = max_money
        
        return max_money