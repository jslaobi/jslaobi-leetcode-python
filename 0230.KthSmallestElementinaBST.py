class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        时间复杂度: O(k + h)，k 为目标顺序，h 为树高。
        空间复杂度: O(h)。
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val
            
            curr = curr.right