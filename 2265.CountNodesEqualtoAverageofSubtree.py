# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes = 0

        def dfs(node: TreeNode) -> tuple:
            if not node:
                return (0, 0)
            
            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)

            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1

            # 题目要求的是向下取整, 所以可以用//
            if current_sum // current_count == node.val:
                self.matching_nodes += 1
            
            return (current_count, current_sum)
        
        dfs(root)

        return self.matching_nodes
