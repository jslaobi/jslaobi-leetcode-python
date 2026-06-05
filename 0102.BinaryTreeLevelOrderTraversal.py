class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        时间复杂度: O(n)，n 为节点个数。
        空间复杂度: O(n)，用于结果列表和队列。
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        if not root:
            return []
        
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_list = []

            for i in range(level_size):
                node = queue.popleft()
                current_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_list[:])
        
        return result