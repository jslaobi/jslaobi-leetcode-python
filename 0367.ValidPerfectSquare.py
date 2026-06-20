class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        if num < 1:
            return False
        
        left = 1
        right = num

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False