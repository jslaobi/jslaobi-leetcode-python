from collections import deque
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional['TreeNode']) -> list[list[int]]:
        if not root:
            return []
        column_map = defaultdict(list)

        queue = deque()
        # queue里面放入Node本身和column index
        queue.append((root, 0))

        min_col = 0
        max_col = 0

        while queue:
            node, col = queue.popleft()
            column_map[col].append(node.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        result = []
        for i in range(min_col, max_col + 1):
            result.append(column_map[i])
        
        return result