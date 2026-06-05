class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        时间复杂度: O(2^n)，n 为数组长度。
        空间复杂度: O(n)，用于递归栈和临时子集。
        """
        result = []
        nums.sort()

        def backtrack(start: int, current_list: List[int]):
            result.append(current_list[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                current_list.append(nums[i])
                backtrack(i+1, current_list)
                current_list.pop()
        
        backtrack(0,[])
        return result