class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        stops = []

        # 加入数组, 起点+num_passengers, 终点-num_passengers
        for num_passengers, start, end in trips:
            stops.append((start, num_passengers))
            stops.append((end, -num_passengers))
        
        # 排序
        stops.sort()

        curr_passengers = 0

        for location, num_passengers in stops:
            curr_passengers += num_passengers
            if curr_passengers > capacity:
                return False
        
        return True
        
        # stops = [0] * 1001

        # for num_passengers, start, end in trips:
        #     stops[start] += num_passengers
        #     stops[end] -= num_passengers

        # curr_passengers = 0

        # for stop in stops:
        #     curr_passengers += stop
        #     if curr_passengers > capacity:
        #         return False
        
        # return True