class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        result = []
        i = 0
        n =len(intervals)

        # 第一组: 在新区间的左边并且完全不沾边
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # 第二组: 与新区间有交集的. 因为intervals是已经排好序的,所以从i当前的位置到intervals[i][0] > newInterval[1]为止都是符合要求的数组
        # i记录的是旧区间而不是result的位置,所以每次循环都要i+=1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)
        

        #第三组: 在新区间的右边并且完全不沾边
        while i < n:
            result.append(intervals[i])
            i += 1

        return result