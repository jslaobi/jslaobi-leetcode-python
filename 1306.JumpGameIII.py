from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """BFS 检查能否到达值为 0 的位置。

        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(n)，用于队列和访问集合。
        """
        queue = deque([start])
        visited = {start}

        while queue:
            current = queue.popleft()

            if arr[current] == 0:
                return True
            
            jump = arr[current]
            left = current - jump
            right = current + jump

            if left >= 0 and left not in visited:
                queue.append(left)
                visited.add(left)
            
            if right < len(arr) and right not in visited:
                queue.append(right)
                visited.add(right)
        
        return False