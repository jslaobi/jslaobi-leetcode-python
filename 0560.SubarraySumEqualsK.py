class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        count = 0
        curr_sum = 0

        # 将0出现的次数记为1次,方便以后计算
        prefix_sums = { 0:1 }
        for num in nums:
            curr_sum += num
            # 查看之前有没有出现curr_sum - k, 如果有的话,则找到了一个和为k的子数组, 获取出现次数并加到count上
            if (curr_sum - k) in prefix_sums:
                count += prefix_sums[curr_sum - k]
            # 无论是否找到符合条件的结果,都要更新prefix_sums
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
        return count