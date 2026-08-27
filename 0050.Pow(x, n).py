class Solution:
    def myPow(self, x: float, n: int) -> float:
        """时间复杂度: O(log n)。
        空间复杂度: O(1)。
        """
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            else:
                x *= x
                n //= 2
        
        return result