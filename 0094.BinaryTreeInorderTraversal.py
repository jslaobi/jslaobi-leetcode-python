class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        时间复杂度: O(n)，n 为节点个数。
        空间复杂度: O(n)，用于结果列表和栈。
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        result = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            result.append(node.val)
            node = node.right
        
        return result

        # Recursive solution:
        # result = []

        # def traverse(node):
        #     if not node:
        #         return
            
        #     traverse(node.left)
        #     result.append(node.val)
        #     traverse(node.right)
        
        # traverse(root)
        # return result