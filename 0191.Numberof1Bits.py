class Solution:
    def hammingWeight(self, n: int) -> int:
        """时间复杂度: O(log n)。
        空间复杂度: O(1)。
        """
        count = 0

        while n:
            n &= (n - 1)
            count += 1
        
        return count