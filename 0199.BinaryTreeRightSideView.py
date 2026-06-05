from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        时间复杂度: O(n)，n 为节点个数。
        空间复杂度: O(n)。
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                # 如果是queue里的最后一个,则是能从右边被看到的元素
                if i == length - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return result