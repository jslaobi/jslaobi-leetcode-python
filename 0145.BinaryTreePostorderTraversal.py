class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
        result = []
        if not root:
            return result

        stack = []
        curr = root
        # 需要last_visited来区分两种情况: 1. 只探索完左边而没有探索右边 2. 已探索完右边
        last_visited = None

        while stack or curr:
            # 先一直向左探到底部
            if curr:
                stack.append(curr)
                curr = curr.left
            
            else:
                peek_node = stack[-1]
                # 分两种情况, 如果右边有节点,且没有探索过右边(last_visited != peek_node.right)
                if peek_node.right and last_visited != peek_node.right:
                    curr = peek_node.right
                # 没有右边节点,或者右边已经探索过,则添加到结果,更新last_visited,并返回上一层(将当前节点移除出stack)
                else:
                    result.append(peek_node.val)
                    last_visited = stack.pop()
        
        return result


        # result = []
        # if not root:
        #     return result
        
        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     result.append(node.val)
        
        # dfs(root)
        # return result