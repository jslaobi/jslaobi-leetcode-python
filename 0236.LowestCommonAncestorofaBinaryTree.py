# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # 找到了p或者q就立刻返回
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果p和q分布在两侧,则root就是公共祖先
        if left and right:
            return root
        # 如果p和q只分布在一侧,那么较高的那个就是公共祖先
        elif left:
            return left
        else:
            return right