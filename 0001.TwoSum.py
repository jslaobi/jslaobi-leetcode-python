class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                # 这里把值存成索引，方便按照值查找
                return [seen[complement], i]
            seen[nums[i]] = i
        return []