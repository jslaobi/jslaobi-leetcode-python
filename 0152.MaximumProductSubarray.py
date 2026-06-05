class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(1)。
        """
        if not nums:
            return 0
        
        current_min = nums[0]
        current_max = nums[0]
        result = nums[0]

        for num in nums[1:]:
            # 如果这里左边写current_max,那么就会更新current_max的值,下面一行计算current_min的时候就会出问题
            # 所以要暂时把计算结果放在临时变量temp_max里,继续之后的计算
            temp_max = max(num, current_min * num, current_max * num)
            current_min = min(num, current_min * num, current_max * num)
            # 计算完成后就可以把current_max更新了
            current_max = temp_max
            # current_min和current_max存储的是每一轮的值,还需要一个全局变量存储最大值
            result = max(result, current_max)
        # 这里也可以分num是正副值两种情况讨论, 示例:
        # if n >= 0:
        #         # Positive number: maintain normal course
        #         # (We still use max(n, ...) to handle the 'Zero Reset')
        #         curr_max = max(n, curr_max * n)
        #         curr_min = min(n, curr_min * n)
                
        #     else:
        #         # Negative number: cross the streams!
        #         # We MUST save curr_max in a temp variable so we don't ruin the curr_min calculation
        #         temp_max = curr_max
                
        #         # Notice we multiply 'n' by curr_MIN to get the new MAX
        #         curr_max = max(n, curr_min * n)
                
        #         # Notice we multiply 'n' by temp_MAX to get the new MIN
        #         curr_min = min(n, temp_max * n)
        return result