class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """稀疏矩阵乘法。

        时间复杂度: O(m * n * k) 最坏情况，m、k、n 分别为矩阵维度。
        空间复杂度: O(m*k + k*n)，用于压缩矩阵存储。
        """
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        result = [[0] * n for _ in range(m)]

        compressed_mat1 = [[] for _ in range(m)]
        for i in range(m):
            for t in range(k):
                if mat1[i][t] != 0:
                    compressed_mat1[i].append((t, mat1[i][t]))

        compressed_mat2 = [[] for _ in range(k)]
        for t in range(k):
            for j in range(n):
                if mat2[t][j] != 0:
                    compressed_mat2[t].append((j, mat2[t][j]))

        for i in range(m):
            for t, val1 in compressed_mat1[i]:
                for j, val2 in compressed_mat2[t]:
                    result[i][j] += val1 * val2

        return result
        # m = len(mat1)
        # k = len(mat1[0])
        # n = len(mat2[0])

        # res = [[0] * n for _ in range(m)]
        
        # for i in range(m):
        #     for t in range(k):
        #         if mat1[i][t] != 0:
        #             for j in range(n):
        #                 if mat2[t][j] != 0:
        #                     res[i][j] += mat1[i][t] * mat2[t][j]  
        
        # return res