# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """时间复杂度: O(n).
        空间复杂度: O(1).
        """
        if not root:
            return None
        
        # 新建两个变量, leftmost指向每层最左边的节点,并且向下移动. current也从每层最左边出发,向右移动
        # 这里的leftmost和current都在当前操作的节点的上层,通过.left,.right来操作当前层的节点
        leftmost = root

        while leftmost.left:
            current = leftmost
            while current:
                # 操作同一节点下的左右子节点
                current.left.next = current.right
                # 操作相邻的两个节点,将前一个节点的右节点指向后一个节点的左节点
                if current.next:
                    current.right.next = current.next.left
                # 向右移向下一个节点
                current = current.next
            # 向下移向下一层
            leftmost = leftmost.left
        
        return root