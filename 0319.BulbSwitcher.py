import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """时间复杂度: O(1)。
        空间复杂度: O(1)。
        """
        return int(math.sqrt(n))