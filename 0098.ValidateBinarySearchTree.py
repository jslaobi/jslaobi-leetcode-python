class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
        stack = []
        node = root
        prev = float('-inf')
        # 使用in order traversal将BST转换为排序好的数组
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val

            node = node.right
        
        return True
            
        # def validate(node, low, high):
        #     # 如果没有子叶,则是有效二叉搜索是
        #     if not node:
        #         return True
            
        #     if not (low < node.val < high):
        #         return False
        #     # 左子叶小于当前值,右子叶大于当前值
        #     return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # return validate(root, float('-inf'), float('inf'))