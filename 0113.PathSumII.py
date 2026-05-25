# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        if not root:
            return result

        def dfs(node, current, current_list):
            if not node:
                return

            current += node.val
            current_list.append(node.val)

            if not node.left and not node.right:
                if current == targetSum:
                    result.append(current_list[:])
            else:
                dfs(node.left, current, current_list) 
                dfs(node.right, current, current_list)

            current_list.pop()
        
        dfs(root, 0, [])

        return result