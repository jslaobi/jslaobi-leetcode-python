class Solution:
    def maxProduct(self, n: int) -> int:
        """时间复杂度: O(log n)。
        空间复杂度: O(1)。
        """
        max1 = 0
        max2 = 0

        while n > 0:
            digit = n % 10

            # 如果比当前最大的数大,将最大的数降为第二大的数,存储新的最大数
            if digit >= max1:
                max2 = max1
                max1 = digit
            elif digit > max2:
                max2 = digit
            
            n //= 10
        
        return max1 * max2