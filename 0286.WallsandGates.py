from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """时间复杂度: O(m * n)。
        空间复杂度: O(m * n)。
        """
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])

        queue = deque()

        EMPTY = 2 ** 31 - 1

        # 从门出发找最近空房间, 首先添加所有的门(0)到queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc] == EMPTY:
                    # 更新距离(当前距离+1)
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
