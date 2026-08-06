class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        """时间复杂度: O(1)。
        空间复杂度: O(1)。
        """
        # 因为以0结尾的数的乘积总是0. 0可以被任何数整除. 所以最多10步就可以找到符合条件的数.
        for num in range(n, n+10):
            product = 1
            temp = num

            while temp > 0:
                digit = temp % 10
                product *= digit
                temp //= 10
            
            if product % t == 0:
                return num