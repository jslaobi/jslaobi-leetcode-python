class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """按螺旋顺序遍历矩阵。

        时间复杂度: O(m*n)，m 和 n 分别为行数和列数。
        空间复杂度: O(1)，不包括结果列表。
        """
        if not matrix or not matrix[0]:
            return []
        
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
            