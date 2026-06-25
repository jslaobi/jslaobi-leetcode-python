import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])

        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            # 如果当前会议的开始时间大于等于最早结束的会议的结束时间, 则说明可以复用这个会议室
            if intervals[i][0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, intervals[i][1])
        
        return len(free_rooms)