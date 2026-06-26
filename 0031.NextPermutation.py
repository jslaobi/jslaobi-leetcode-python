class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
            时间复杂度: O(n)。
            空间复杂度: O(1)。
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        # 从后往前,找到第一个出现前一个数字比后一个小的情况. 比如13542, 542这种降序排列是没法通过重组获得下一个更大的数, 524或者452都是更小的数
        # 而3比5小,这种情况下就会有可能找到下一个更大的数
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 但是我们不想直接交换,因为15342可能不是下一个最接近的更大的数. 因为542是降序,所以我们要从最后一位向前寻找第一个比3大的数,然后跟3进行交换
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # 如果整个数组都是倒序,如54321, 则不可能有下一个更大值. 按照题目要求, 需要输出最小值,简单进行一个倒序排列就是最小值
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1