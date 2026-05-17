class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            last_added = result[-1]

            # 注意这里是interval[0]而不是intervals[0], interval[0]和[1]分别表示区间的开头和结尾
            # 如果上次添加的区间和新区间有重合,则合并两个区间
            if last_added[1] >= interval[0]:
                last_added[1] = max(last_added[1], interval[1])
            else:
                result.append(interval)
        
        return result

