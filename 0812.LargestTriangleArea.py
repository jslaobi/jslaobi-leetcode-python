import itertools

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """时间复杂度: O(n^3)。
        空间复杂度: O(1)。
        """
        max_area = 0.0
        
        def get_area(p1, p2, p3):
            return 0.5 * abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            )
        
        for p1, p2, p3 in itertools.combinations(points, 3):
            max_area = max(max_area, get_area(p1, p2, p3))
        
        return max_area