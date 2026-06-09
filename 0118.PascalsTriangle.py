class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [[1]]

        for i in range(1, numRows):
            prev_row = result[-1]
            curr_row = [1]

            # 比如第4行, i=3. range(1, i)只处理中间两个数:1和2. 0和3会在前后被赋值为1
            # prev_row = [1, 2, 1]
            # new_row = [1, 3, 3, 1]
            # Index:         0    1    2    3
            # ---------------------------------
            # prev_row:    [ 1,   2,   1 ]
            #                | \  | \  |
            # new_row:     [ 1,   3,   3,   1 ]
            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])
            curr_row.append(1)
            result.append(curr_row)
            
        return result
  