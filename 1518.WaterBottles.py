class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        result = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            leftover_empties = empty_bottles % numExchange
            result += new_bottles
            empty_bottles = new_bottles + leftover_empties
        
        return result