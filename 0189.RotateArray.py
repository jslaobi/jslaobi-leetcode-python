class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        n = len(nums)
        # k有可能比n大, 所以取模把多余的部分去掉
        k = k % n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # 三部曲: 1. 整体反转 2. 前k个反转 3. 第k个之后反转, 即可完成rotate操作   
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return nums
