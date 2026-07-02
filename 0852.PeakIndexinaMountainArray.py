class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            # 如果是上坡, 结果一定在右边,移动左指针
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            # 如果是下坡,结果一定在左边,移动右指针
            else:
                right = mid
        
        return left
