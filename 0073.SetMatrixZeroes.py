class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
            时间复杂度: O(m*n)。
            空间复杂度: O(1)。
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # 使用第一行和第一列来标记每隔行列是否有0
        # matrix[0][0]是第一行和第一列的重合点,所以无法直接判断是否代表的行还是列,所以需要借助is_row_zero变量
        is_row_zero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        is_row_zero = True

        # 先处理除第一行和第一列的0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if is_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        # rows = len(matrix)
        # cols = len(matrix[0])

        # rows_with_zero = set()
        # cols_with_zero = set()

        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == 0:
        #             rows_with_zero.add(r)
        #             cols_with_zero.add(c)
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if r in rows_with_zero or c in cols_with_zero:
        #             matrix[r][c] = 0
        