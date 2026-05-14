class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Two-sum via hash map.

        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(n)，用于存储已访问元素的哈希映射。
        """
        seen = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                # 这里把值存成索引，方便按照值查找
                return [seen[complement], i]
            seen[nums[i]] = i
        return []