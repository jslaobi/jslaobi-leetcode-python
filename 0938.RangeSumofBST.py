# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(h)。
        """
        if not root:
            return 0
        
        # 如果当前值大于high, 需要向左探索
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # 如果当前值小于low, 需要向右探索
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # 如果当前值在low与high之间,则加到总和
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        
