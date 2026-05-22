class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """双指针查找两个有序数组的最小公共值。

        时间复杂度: O(n+m)，n 和 m 分别为两个数组长度。
        空间复杂度: O(1)。
        """
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return -1