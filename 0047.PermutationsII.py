class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 有重复数字去重一定要排序
        nums.sort()
        used = [False] * len(nums)

        def dfs(current_list: List[int]):
            if len(current_list) == len(nums):
                result.append(current_list[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # not used[i - 1]而不是not used[i]的原因是, [1,1]第一个可以把两个1加进去,但是第二个就不允许加了,达到去重的效果
                # 如果有多个1也是同理,不停的向前检查,达到去重的效果
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                current_list.append(nums[i])
                dfs(current_list)
                current_list.pop()
                used[i] = False
        
        dfs([])
        return result