class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        时间复杂度: O(n+m)。
        空间复杂度: O(min(n,m))。
        """
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        # 题目要求结果里的数字不重复, 比如例子1, 结果里只有1个2.
        result = set()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return list(result)