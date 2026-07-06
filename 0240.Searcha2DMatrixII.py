class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        # 从右上角开始,向左寻找更小值,向下寻找更大值
        row = 0
        col = n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False