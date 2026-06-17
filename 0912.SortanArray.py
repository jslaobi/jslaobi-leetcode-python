class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 我们实现merge sort
        def merge_sort(left, right):
            if left >= right:
                return
            mid = left + (right - left) // 2
            
            # 使用递归给左右两部分排序
            merge_sort(left, mid)
            merge_sort(mid+1, right)

            # 将排好序的两部分合并
            merge(left, mid, right)

        def merge(left, mid, right):
            temp = []
            # 左半边数组从最左边开始
            i = left
            # 右半边数组从mid+1开始
            j = mid + 1

            # 把左右两边的数合并在一起
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            # 如果左边或者右边还有剩余的数
            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1
            
            # 把排好序的数组写回原数组, 从left开始(因为要在原数组上操作)
            for k in range(len(temp)):
                nums[left + k] = temp[k]
        
        merge_sort(0, len(nums) - 1)

        return nums