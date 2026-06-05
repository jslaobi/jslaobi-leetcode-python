class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """
        时间复杂度: O(n)，n 为公交站数量。
        空间复杂度: O(1)。
        """
        if start > destination:
            start, destination = destination, start
        
        clockwise_distance = sum(distance[start: destination])
        total_distance = sum(distance)
        counterclockwise_distance = total_distance - clockwise_distance

        return min(clockwise_distance, counterclockwise_distance)