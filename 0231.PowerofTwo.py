class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        时间复杂度: O(log n)，n 为输入值。
        空间复杂度: O(1)。
        """
        if n <= 0:
             return False
        
        while n % 2 == 0:
            n = n // 2
        
        return n == 1