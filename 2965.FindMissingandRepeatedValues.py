class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        时间复杂度: O(n^2)。
        空间复杂度: O(1)。
        """
        n = len(grid)
        counts = [0] * (n * n + 1)

        for row in range(n):
            for col in range(len(grid[0])):
                num =  grid[row][col] 
                counts[num] += 1
        
        repeated_num = -1
        missing_num = -1

        for i in range(1, len(counts)):
            if counts[i] == 2:
                repeated_num = i
            elif counts[i] == 0:
                missing_num = i
        
        return [repeated_num, missing_num]