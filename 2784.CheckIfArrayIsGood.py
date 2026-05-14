class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """检查数组是否满足题目要求。

        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(n)，用于计数器存储元素出现次数。
        """
        n = len(nums) - 1
        # 如果连[1,1]都不满足,即长度小于2-1=1,则直接返回False
        if n < 1:
            return False

        counts = Counter(nums)
        # 分两部分处理,首先处理到n-1的部分,因为不存在base[0]这种情况,所以从1开始处理
        for i in range(1, n):
            if counts[i] != 1:
                return False
        # 最后处理n的部分,如果n出现两次则满足条件,否则不满足
        return True if counts[n] == 2 else False
