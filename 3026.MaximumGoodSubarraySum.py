import math

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # 实时更新的最大值,将来作为函数返回值
        result = -math.inf
        # 当前处理的数为止的数字和
        curr_sum = 0
        # 到每个数字为止的和 - 不包括当前数字, 这也就是为什么叫prefix
        min_prefix = {}

        for num in nums:
            # 比当前数字小k的值和比当前数字大k的值都符合条件
            if (num - k) in min_prefix:
                # 这里还不能更新curr_sum,以后还要继续使用,所以使用临时变量
                # 到当前为止的和, 加上当前数字, 减去到num - k的和,就是子数组的最大和
                temp_sum = curr_sum + num - min_prefix[num - k]
                result = max(result, temp_sum)
            if (num + k) in min_prefix:
                # 到当前为止的和, 加上当前数字, 减去到num + k的和,就是子数组的最大和
                temp_sum = curr_sum + num - min_prefix[num + k]
                result = max(result, temp_sum)
            # 这里不能直接else
            # 如果不在prefix里, 就把curr_sum存入
            # 如果curr_sum比已经在min_prefix里的值小,也可以更新. 因为公式是curr_sum + num - min_prefix, min_prefix越小,得到的结果越大
            # 如果curr_sum大于min_prefix已有的值,则不更新. 原理如上
            if num not in min_prefix or curr_sum < min_prefix[num]:
                min_prefix[num] = curr_sum
            # 最后更新curr_sum
            curr_sum += num
        
        return result if result != -math.inf else 0
