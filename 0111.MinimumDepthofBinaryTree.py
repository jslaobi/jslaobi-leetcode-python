class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        时间复杂度: O(n)，n 为节点个数。
        空间复杂度: O(h)，h 为树高。
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        depth = 1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth
        # if not root:
        #     return 0
        
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))