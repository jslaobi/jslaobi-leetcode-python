class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """时间复杂度: O(h)。
        空间复杂度: O(1)。
        """
        closest = root.val
        curr = root

        while curr:
            if abs(curr.val - target) < abs(closest - target):
                closest = curr.val
            elif abs(curr.val - target) == abs(closest - target):
                closest = min(closest, curr.val)
                
            if target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
            else:
                break
        
        return closest