class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(1)。
        """
        if not intervals:
            return 0
        
        # 按照end time排序
        intervals.sort(key=lambda x:x[1])

        intervals_to_keep = 1

        end = intervals[0][1]

        for i in range(1, len(intervals)):
            # 如果没有overlap, 则可以保留, 并且继续扩展end
            if intervals[i][0] >= end:
                end = intervals[i][1]
                intervals_to_keep += 1
        
        # 总长度减去要保留的,就是要去除的
        return len(intervals) - intervals_to_keep