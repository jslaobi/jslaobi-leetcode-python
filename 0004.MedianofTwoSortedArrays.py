import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 把长度较小的放在前面, 这样等下计算partitionY = (m + n + 1) // 2 - partitionX的时候不出出现负数index
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m

        while low <= high:
            partition_x = low + (high - low) // 2
            # 这里使用m + n + 1,保证如果是奇数的情况,则目标值落在前半边. 
            # 如果写成m + n也可以,这样就会保证落在后半边, 之后用return min(min_left_x, min_left_y)来取即可
            partition_y = (m + n + 1) // 2 - partition_x

            if partition_x == 0:
                max_left_x = -math.inf
            else:
                max_left_x = nums1[partition_x - 1]

            if partition_x == m:
                min_right_x = math.inf
            else:
                min_right_x = nums1[partition_x]
            
            if partition_y == 0:
                max_left_y = -math.inf
            else:
                max_left_y = nums2[partition_y - 1]

            if partition_y == n:
                min_right_y = math.inf
            else:
                min_right_y = nums2[partition_y]

            # 如果第一组的左边最大值小于第二组的右边最小值, 第二组的左边最大值小于第一组的右边最小值,我们就找到了目标值
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # 如果是偶数,就取左边最大和右边最小的平均值,比如题目例子2: Input: nums1 = [1,2], nums2 = [3,4]Output: 2.50000
                if (m + n) % 2 ==0:
                    left_max = max(max_left_x, max_left_y)
                    right_min = min(min_right_x, min_right_y)
                    return (left_max + right_min) / 2
                # 如果是偶数, 则取左边的最大值(之前(m + n + 1)保证了最大值落在左边)
                else:
                    return max(max_left_x, max_left_y)

            # 这里的low, high,partition_x都是在操作nums1数组
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else: 
                low = partition_x + 1




