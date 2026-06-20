# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        时间复杂度: O(m * n)，
        空间复杂度: O(1)。
        """
        rows, cols = binaryMatrix.dimensions()

        row = 0
        col = cols - 1

        leftmost_col = -1

        while row < rows and col >= 0:
            # 如果当前是1, 更新leftmost_col并且继续往左找
            if binaryMatrix.get(row, col) == 1:
                leftmost_col = col
                col -= 1
            # 如果是0, 因为每一行都是排好序的,所以再往左边找也不会有1了, 继续往下一行找
            else:
                row += 1
            
        return leftmost_col
        
        # rows, cols = binaryMatrix.dimensions()
        
        # # We initialize to 'cols' (out of bounds) so we can track the minimum
        # leftmost_col = cols
        
        # for row in range(rows):
        #     # Standard Binary Search pointers
        #     left = 0
            
        #     # OPTIMIZATION: We strictly bound our search space to columns smaller 
        #     # than our current best answer. If we haven't found a 1 yet, it searches the whole row.
        #     right = leftmost_col - 1 
            
        #     while left <= right:
        #         mid = left + (right - left) // 2
                
        #         if binaryMatrix.get(row, mid) == 1:
        #             # We found a 1! Update our best answer.
        #             leftmost_col = mid
                    
        #             # We continue searching to the left to see if there's an even earlier 1 in this row.
        #             right = mid - 1
        #         else:
        #             # We found a 0. The first 1 (if it exists) must be to the right.
        #             left = mid + 1
                    
        # # If leftmost_col never changed from our initial out-of-bounds value, the matrix is all 0s.
        # if leftmost_col == cols:
        #     return -1
        # else:
        #     return leftmost_col