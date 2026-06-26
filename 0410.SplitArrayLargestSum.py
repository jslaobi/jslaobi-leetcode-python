class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        时间复杂度: O(n log(sum(nums)))。
        空间复杂度: O(1)。
        """
        def can_split(target_sum: int) -> bool:
            curr_sum = 0
            num_of_subarrays = 1

            for num in nums:
                curr_sum += num
                # 如果当前sum超了, 则需要创建一个新的子数组
                if curr_sum > target_sum:
                    num_of_subarrays += 1
                    curr_sum = num

                if num_of_subarrays > k:
                    return False
            
            return True

        # 最小的可能是每个数都是一个子数组, 那么最小值就是数组里的最大值
        left = max(nums)
        # 最小的可能是所有数都在一个子数组, 那么最小值就是数组的和
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2

            # 如果当前的数可以成功分成k组,继续向左寻找更小的可能的和
            if can_split(mid):
                right = mid
            # 如果不能分, 则当前的数太小, 需要放大
            else:
                left = mid + 1
            
        return left