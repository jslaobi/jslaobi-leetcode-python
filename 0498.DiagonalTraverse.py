from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        # 相同的行和列和的数字, 在同一条对角线上
        # Diagonal 0 (sum = 0): (0, 0)

        # Diagonal 1 (sum = 1): (0, 1), (1, 0)

        # Diagonal 2 (sum = 2): (0, 2), (1, 1), (2, 0)
        diagonals = defaultdict(list)

        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
        
        result = []

        # 最大的r + c的和是(m - 1) + (n - 1)
        # 奇数和偶数的方向不一样, 偶数往右上,所以要reverse. 奇数往左下,可以输出正常序列
        for i in range(m + n - 1):
            if i % 2 == 0:
                # 因为result是个1d array [1,2,4,7,5,3,6,8,9], 所以要用extend添加元素进result数组
                result.extend(diagonals[i][::-1])
            else:
                result.extend(diagonals[i])
        
        return result

        