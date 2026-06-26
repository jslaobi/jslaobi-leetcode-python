from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        # Initialize our podium with negative infinity
        first = second = third = float('-inf')
        
        for num in nums:
            # Rule 4: Ignore numbers that are already on the podium
            if num in (first, second, third):
                continue
                
            # Rule 1: We found a new Gold! Shift everyone down.
            if num > first:
                third = second
                second = first
                first = num
                
            # Rule 2: We found a new Silver! Shift Bronze down.
            elif num > second:
                third = second
                second = num
                
            # Rule 3: We found a new Bronze! Just replace it.
            elif num > third:
                third = num
                
        # The problem states: "If the third maximum does not exist, return the maximum"
        # We check if 'third' is still negative infinity to know if it was ever updated.
        if third == float('-inf'):
            return first
        else:
            return third