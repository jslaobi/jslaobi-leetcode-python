class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
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
        def check_height(node):
            if not node:
                return 0
            
            # 如果左半边已经不平衡,则直接返回-1
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            # 如果右半边已经不平衡,则直接返回-1
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            # 否则,检查当前左半边和右半边是否平衡
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        if check_height(root) == -1:
            return False
        else:
            return True