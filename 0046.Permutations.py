class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯生成所有排列。

        时间复杂度: O(n * n!)，n 为数组长度。
        空间复杂度: O(n)，用于递归栈和临时排列。
        """
        result = []

        def dfs(current_list: List[int]):
            if len(current_list) == len(nums):
                result.append(current_list[:])
                return

            for num in nums:
                if num in current_list:
                    continue
                    
                current_list.append(num)
                dfs(current_list)
                current_list.pop()

        dfs([])
        return result