class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        n = len(nums)
        counts = [0] * n

        # 之后排序会乱序, 所以我们存储原始index+数字
        # 示例: [(0, nums[0]), (1, nums[1]), ...]
        enum_nums = list(enumerate(nums))

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                # 如果左边的更小,则取左边
                # left[i][0]是原始index, left[i][1]是数字
                if left[i][1] <= right[j][1]:
                    original_index = left[i][0]
                    # j向前移动了几位,就说明右边有j个更小的数字,加到结果里
                    counts[original_index] += j
                    # merged存储排序好的数组, 示例: [(3, 1), (1, 2), (0, 5), (2, 6)], 第一位是原始index,第二位是数字
                    merged.append(left[i])
                    i += 1
                else:
                    # 右边的数字更小, 移动j, 将右边添加到merged数组
                    merged.append(right[j])
                    j += 1
            
            # 如果循环后左边或者右边还有剩余, 则对左边或者右边单独进行merge(与上面代码完全相同)
            while i < len(left):
                original_index = left[i][0]
                counts[original_index] += j
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(enum_nums)
        return counts