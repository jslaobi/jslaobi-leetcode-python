class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        # 因为允许重复一次,所以2个元素肯定是满足条件的
        n = len(nums)
        if n <= 2:
            return len(nums)
        # slow指向当前需要操作的元素, 不用担心错过前两个元素,因为一会会用slow-2进行对比
        slow = 2

        for fast in range(2, n):
            # slow-2: 慢指针的比较元素, slow: 当前需要操作替换的元素, fast: 快指针的比较元素
            # 如果不相等,就证明没有出现超过2个相同元素,可以把fast挪到slow
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            # 否则,就证明出现了超过2个相同元素,让循环继续以跳过这个元素,fast+1
        return slow