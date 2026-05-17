class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 从后向前解法:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # 如果当年的位置加上能走的步数能达到终点, 那么就把终点移到当前位置,然后继续检查
            if (i + nums[i]) >= goal:
                goal = i
            # 否则就继续向前检查是否有其他位置满足条件

        # 最后检查是否能将位置成功移动到开头
        return goal == 0

        # 从前向后解法:
        # max_reach = 0
        # goal = len(nums) - 1

        # for i in range(len(nums)):
        #     # 如果已经超过了能跳跃的最大步数,则返回False
        #     if i > max_reach:
        #         return False
        #     # 检查是否需要更新最大步数
        #     reach = i + nums[i]
        #     max_reach = max(reach, max_reach)

        #     if max_reach >= goal:
        #         return True

        # return False