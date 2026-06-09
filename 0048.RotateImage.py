class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        # 一层一层逐渐向内圈处理
        while left < right:
            for i in range(right - left):
                # 因为是一圈一圈处理的, 所以每一圈top+1时,left也+1. bottom-1时,right也-1
                top = left
                bottom = right

                # 左上角向右移动,所以left + i
                temp = matrix[top][left + i]
                # 把左下移动到左上
                # 左下角向上移动,所以bottom - i
                matrix[top][left + i] = matrix[bottom - i][left]
                # 把右下移动到左下
                # 右下角向左移动,所以right - i
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # 把右上移动到右下
                # 右上角向下移动,所以top + i
                matrix[bottom][right - i] = matrix[top + i][right]
                # 把之前保存的左上移动到右上
                matrix[top + i][right] = temp

            left += 1
            right -= 1

