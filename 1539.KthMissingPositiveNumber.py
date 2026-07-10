class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """时间复杂度: O(log n)。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # 因为数组是以0起始,所以index要加1,也就是mid+1
            # missing_count计算有多少个缺失数字
            missing_count = arr[mid] - (mid + 1) 
            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left + k