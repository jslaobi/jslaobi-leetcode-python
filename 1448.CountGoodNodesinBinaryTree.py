# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(h)。
        """
        
        def dfs(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0
            
            is_good = 0

            # 如果当前node的值大于max_so_far, 则符合goog node的条件
            if node.val >= max_so_far:
                is_good = 1
            
            max_so_far = max(max_so_far, node.val)

            is_good += dfs(node.left, max_so_far)
            is_good += dfs(node.right, max_so_far)

            return is_good
        
        return dfs(root, root.val)