class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        a = p
        b = q

        while a != b:
            if a.parent is not None:
                a = a.parent
            else:
                a = q

            if b.parent is not None:
                b = b.parent
            else:
                b = p
                
        return a