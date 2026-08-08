from collections import Counter

class DetectSquares:

    def __init__(self):
        """时间复杂度: O(1)。
        空间复杂度: O(1)。
        """
        self.point_counts = Counter()

    def add(self, point: List[int]) -> None:
        """时间复杂度: O(1)。
        空间复杂度: O(1)。
        """
        # 将list转换为tuple, 才能作为key
        self.point_counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        point_x, point_y = point
        total_squares = 0

        for (x, y), point_count in self.point_counts.items():
            # 检查(x, y)和(point_x, point_y)能否组成正方形
            # 1. 水平和垂直距离必须相等
            # 2. 不能是同一个点
            if abs(point_x - x) == abs(point_y - y) and point_x != x:
                # 找到了两个点, 剩下的两个点必须在(x, point_y) 和 (point_x, y)
                corner1_count = self.point_counts[(x, point_y)]
                corner2_count = self.point_counts[(point_x, y)]

                total_squares += point_count * corner1_count * corner2_count
        
        return total_squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)