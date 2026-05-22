class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯寻找不重复的组合总和。

        时间复杂度: O(2^n)（指数级），n 为候选项数量。
        空间复杂度: O(n)，递归栈深度和当前组合列表。
        """
        result = []
        candidates.sort()

        def backtrack(start_index: int, current_list: List[int], current_sum: int):
            if current_sum == target:
                result.append(current_list[:])
                return
            elif current_sum > target:
                return
            else:
                for i in range(start_index, len(candidates)):
                    # 如果跟上一个数字一样,且不是第一个数字,则认定为重复并跳过
                    if i > start_index and candidates[i] == candidates[i - 1]:
                        continue
                    elif start_index > len(candidates):
                        return
                    else:
                        # 分三步走, 和39题一样,一定不要试图合并第一步和第二步
                        current_list.append(candidates[i])
                        # 这里跟39题不一样,因为不许有重复数字,所以直接传入i + 1
                        backtrack(i + 1, current_list, current_sum + candidates[i])
                        current_list.pop()

        backtrack(0, [], 0)

        return result