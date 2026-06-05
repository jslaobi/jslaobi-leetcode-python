class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(log n)，递归栈深度。
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        def build_bst(left, right):
            if left > right:
                return None
            
            mid = left + (right - left) // 2

            root = TreeNode(nums[mid])

            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)

            return root
        
        return build_bst(0, len(nums) - 1)