class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i: int, current_list: List[int], current_sum: int):
            if current_sum == target:
                result.append(current_list[:])
                return

            if current_sum > target or i >= len(candidates):
                return

            # 分三步走, 一定不要试图合并第一步和第二步, current_list.append(candidates[i])会返回None
            # 而且即使写法正确,也会多占用空间,因为程序会每次复制一个新的list
            current_list.append(candidates[i])
            backtrack(i, current_list, current_sum + candidates[i])
            current_list.pop()

            backtrack(i + 1, current_list, current_sum)

        backtrack(0, [], 0)

        return result
        
