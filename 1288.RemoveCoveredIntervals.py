class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 按照起始时间正序, 如果相同的起始时间则结束时间倒序
        intervals.sort(key=lambda x:(x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            # 因为是排好序的,所以start一定是越来越往右,只需要看end是否被包含
            if end > max_end:
                count += 1
                max_end = end
        
        return count
