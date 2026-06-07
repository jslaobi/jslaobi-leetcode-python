# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 将node存在hashmap里,方便直接查找到任何node. key是值,value是node本身
        nodes = {}
        # 保存所有的子节点,最后不在set里的就是root
        children = set()

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            if is_left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            children.add(child)

        for parent, _, _ in descriptions:
            if parent not in children:
                return nodes[parent]
