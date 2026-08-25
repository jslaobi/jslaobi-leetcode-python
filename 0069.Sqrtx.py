class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 0
        right = x

        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                result = mid
                left = mid + 1
            else:
                return mid
        
        return result