from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """时间复杂度: O(m*n)。
        空间复杂度: O(m*n)。
        """
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                # 将1设置成一个不可能的距离,比如-1. 这样就不需要额外的visited数组. 设为-1是为了防止原来的1和距离1混淆
                else:
                    mat[r][c] = -1
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat