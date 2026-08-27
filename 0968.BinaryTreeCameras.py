# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(h)。
        """
        self.cameras = 0

        # 0 - 未被覆盖
        # 1 - 有照相机
        # 2 - 已被覆盖/空节点不需要覆盖
        def dfs(node):
            if not node:
                return 2
            
            left_state = dfs(node.left)
            right_state = dfs(node.right)


            # 如果任何子节点是0, 我们必须要放置一个照相机
            if left_state == 0 or right_state == 0:
                self.cameras += 1
                return 1
            
            # 如果任何子节点是1, 当前节点已被覆盖,返回2
            if left_state == 1 or right_state == 1:
                return 2
            
            # 两个子节点都是2, 说明子节点都被覆盖, 但是当前节点没被覆盖. 返回0, 这样父节点可以覆盖它.
            return 0
        
        # edge case: 如果返回0的是根节点, 则需要再加一个照相机覆盖
        if dfs(root) == 0:
            self.cameras += 1
        
        return self.cameras
