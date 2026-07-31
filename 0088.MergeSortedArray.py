class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """时间复杂度: O(m + n)。
        空间复杂度: O(1)。
        """
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = m - 1
        n2 = n - 1
        length = m + n -1
        # 从后往前将大的数放到nums1数组的后端,这样就不用新建数组,达到O(1)的空间复杂度
        # 这里只需要检查n2, 因为当n2没有剩余数字,n1就已经自然排好序了.而当n1没有剩余数字,我们还可以继续正常处理n2
        while n2 >= 0:
            # 这里要检查n1是否为空,如果为空则只需要处理n2
            if n1 >= 0  and nums1[n1] > nums2[n2]:
                nums1[length] = nums1[n1]
                n1 -= 1
            else:
                nums1[length] = nums2[n2]
                n2 -= 1

            length -= 1 
        
        return nums1