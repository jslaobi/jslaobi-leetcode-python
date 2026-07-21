class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """时间复杂度: O(m*n)。
        空间复杂度: O(m*n)。
        """
        # 先转换成1d array, 进行位移,然后再转换回2d array
        m = len(grid)
        n = len(grid[0])
        total = m * n

        # 如果k比total大,先取模到k之内
        k = k % total
        
        if k == 0:
            return grid
        
        flat_list = []

        for row in grid:
            for num in row:
                flat_list.append(num)
        
        # 位移数组. flat_list[-k:] = 倒数k个数字 flat_list[:-k] = 从开头到倒数第k个数字
        shifted_list = flat_list[-k:] + flat_list[:-k]

        result = []
        for i in range(m):
            start_index = i * n
            end_index = (i+1) * n
            result.append(shifted_list[start_index: end_index])
        
        return result