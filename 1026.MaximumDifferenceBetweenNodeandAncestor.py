class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
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
        
        def dfs(node, min_value: int, max_value: int):
            if not node:
                return max_value - min_value
            
            min_value = min(min_value, node.val)
            max_value = max(max_value, node.val)

            left_diff = dfs(node.left, min_value, max_value)
            right_diff = dfs(node.right, min_value, max_value)

            return max(left_diff, right_diff)
        
        return dfs(root, root.val , root.val)