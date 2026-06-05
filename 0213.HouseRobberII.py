class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，n 为房间数量。
        空间复杂度: O(1)。
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def do_rob(nums: List[int]) -> int:
            # rob1 - 两步之前 rob2 - 一步之前 max_money - 当前
            rob1 = 0
            rob2 = 0
            max_money = 0

            for num in nums:
                max_money = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = max_money
            
            return max_money
        # 当房屋成环形,则有两种情况:
        # 1. 抢劫第一间房,不抢最后一间
        # 2. 不抢第一间房,抢劫最后一间
        return max(do_rob(nums[:-1]), do_rob(nums[1:]))