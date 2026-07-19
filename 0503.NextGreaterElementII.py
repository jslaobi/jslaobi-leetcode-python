class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        n = len(nums)

        result = [-1] * n
        # stack存储index,通过nums[stack[i]]来获取真正的数
        stack = []

        # 遍历循环两遍来模拟环形数组, i % n来获取index并且防止溢出
        for i in range(2 * n):
            curr_index = i % n

            # 如果当前的数比stack顶部的数大, 我们就找到了一个符合条件的数, 从stack中pop, 并且用当前的值来添加到result
            while stack and nums[curr_index] > nums[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = nums[curr_index]
            
            # 只有第一遍扫描是添加到stack的过程,第二遍扫描只从stack中pop符合条件的数
            if i < n:
                stack.append(curr_index)
            
        
        return result