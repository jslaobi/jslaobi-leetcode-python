class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(1)。
        """
        # 这道题可以连续反转同一个数, 策略是首先把所有的负数的变成正数
        # 如果之后还有剩余次数,找一个最小的正数,如果剩余偶数次,则不需要做任何操作,如果是奇数,则把那个最小的正数变为负数
        nums.sort(key=abs, reverse=True)

        for i in range(len(nums)):
            if nums[i] <= 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        
        if k % 2 == 1:
            nums[-1] = -nums[-1]
        
        return sum(nums)