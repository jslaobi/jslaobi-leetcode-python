class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先排序，这样方便去重，方便查找，而且这道题总体的复杂度是O(n^2), 排序的时间复杂度是O(nlogn)，所以排序相当于是免费的
        nums.sort()
        result = []
        length = len(nums)

        # 从左边开始遍历，固定一个数i，然后在剩下的数中使用双指针left和right来寻找另外两个数，使得三个数的和为0
        for i in range(length):
            # 这道题有两步去重的地方，这里是第一步，在遍历开始的地方
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left],nums[right]])
                    left += 1
                    # 这道题有两步去重的地方，这里是第二步，在找到一个满足条件的组合之后，继续移动left指针，跳过重复的数
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return result