class Solution:
    def sumAndMultiply(self, n: int) -> int:
        """
        时间复杂度: O(n*d)。
        空间复杂度: O(1)。
        """
        n = abs(n) 
        
        x = 0
        digit_sum = 0
        multiplier = 1
        
        while n > 0:
            digit = n % 10
            n //= 10  
            
            if digit != 0:
                digit_sum += digit
                x += digit * multiplier
                multiplier *= 10
                
        return x * digit_sum