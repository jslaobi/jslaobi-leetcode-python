class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
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
        self.max_sum = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0
            # 选项1: 以当前节点加上左右子树之和构成最大和(在此中止,不可再向上添加新的节点)
            # 值有可能为负数,如果为负数则不选取该子树
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            current_max = node.val + left_gain + right_gain
            
            self.max_sum = max(self.max_sum, current_max)
            # 选项2: 在当前左右子树选其一,并且继续向上添加更多节点
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)

        return self.max_sum