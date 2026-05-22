class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯生成子集。

        时间复杂度: O(2^n)，n 为数组长度。
        空间复杂度: O(n)，用于递归栈和临时子集。
        """
        result = []

        def dfs(i, current):
            #下面无论是否添加当前数字,i都会i+1, 所以空数组或者[1]这些情况都会最终达到i == len(nums)
            if i == len(nums):
                result.append(current[:])
                return
            # 1. 添加当前数字
            current.append(nums[i])
            dfs(i+1, current)
            current.pop()
            # 2. 不添加当前数字
            dfs(i+1, current)
        
        dfs(0,[])
        return result
            
