class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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