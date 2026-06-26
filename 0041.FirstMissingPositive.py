class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        n = len(nums)

        for i in range(n):
            # 注意这里是while循环而不是if, 在每一个位置需要不停的交换,直到1.不在有效范围内,比如0或者负数. 2. 当前位置交换到了正确的数字
            # nums[nums[i] - 1] != nums[i]: 比如当前i=2, num[i]是3, nums[i] - 1是2. nums[2] == 3,也就是nums[3-1] == 3
            
            while 1<= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                curr_index = nums[i] - 1
                nums[i], nums[curr_index] = nums[curr_index], nums[i]
            
        # 第二遍扫描缺少的数字
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1
                