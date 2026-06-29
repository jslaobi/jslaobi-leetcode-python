from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        时间复杂度: O(n log n)。
        空间复杂度: O(1)。
        """
        # 按照会议的开始时间排序
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            # 如果当前会议的开始时间小于前一个会议的结束时间, 则说明有重叠
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True