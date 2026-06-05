from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        时间复杂度: O(max_limit)，max_limit 为搜索上限。
        空间复杂度: O(max_limit)。
        """
        # 为防止无限跳下去,计算上限为最远的forbidden或者家的位置的最大值,
        max_limit = max(max(forbidden) if forbidden else 0, x) + a + b
        # 转换成set优化搜索时间
        forbidden_set = set(forbidden)

        queue = deque()
        total_steps = 0

        # 当前位置,能否向后跳
        queue.append((0, True))

        # 这里也要存储能否向后跳, 例如当从另一个位置向后跳到10, visited = {(10, False)}, 之后又向前跳到了10, visited = {(10, False), (10, True)}, 并且可以继续
        # 只有当再次出现(10, False)或(10, True)时, 才会中止
        visited = {(0, True)}

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr_position, can_jump_forward = queue.popleft()
                
                if curr_position == x:
                    return total_steps
                
                # 第一步: 向前跳
                next_position = curr_position + a
                if next_position <= max_limit and next_position not in forbidden_set:
                    if (next_position, True) not in visited:
                        visited.add((next_position, True))
                        queue.append((next_position, True))
                
                # 第二步: 向后跳
                if can_jump_forward:
                    next_position = curr_position - b
                    if next_position >= 0 and next_position not in forbidden_set:
                        if (next_position, False) not in visited:
                            visited.add((next_position, False))
                            queue.append((next_position, False))
            
            total_steps += 1

        
        return -1

