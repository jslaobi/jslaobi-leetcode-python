class Solution:
    def mySqrt(self, x: int) -> int:
        """二分查找求平方根。

        时间复杂度: O(log x)，x 为输入值。
        空间复杂度: O(1)。
        """
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