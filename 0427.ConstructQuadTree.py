"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, length):
            if length == 1:
                is_one = grid[r][c] == 1
                return Node(is_one, True, None, None, None, None)
            
            half = length // 2

            top_left = dfs(r, c, half)
            top_right = dfs(r, c + half, half)
            bottom_left = dfs(r + half, c, half)
            bottom_right = dfs(r + half, c + half, half)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True, None, None, None, None)

            else:
                return Node(False, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(0, 0, len(grid))