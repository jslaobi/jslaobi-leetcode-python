# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            True
        
        def symmetricTree(left, right):
            if not left and not right:
                return True
            if left and not right:
                return False
            if not left and right:
                return False
            if left.val != right.val:
                return False
            
            return symmetricTree(left.left, right.right) and symmetricTree(left.right, right.left)
        
        return symmetricTree(root.left, root.right)