class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid

            if squared == x:
                return mid
            elif squared > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right