import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """时间复杂度: O((n + q) log n)。
        空间复杂度: O(n)。
        """
        # 按照start time排序
        intervals.sort(key=lambda x:x[0])

        # 这里按照queries的值排序,同时还要保留原有的index
        sorted_queries = sorted([(q, i) for (i, q) in enumerate(queries)])

        result = [-1] * len(queries)

        # 存储(interval_size, right_end)
        min_heap = []

        i = 0

        for query, original_index in sorted_queries:
            # 1. 将所有的start time在当前query之前interval加入heap
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i += 1
            
            # 2. 移除end time在query之前的interval, 清理heap
            # 注: 我们可以在第一步检查end time是否在query之后, 但是即使如此,第二步仍然必不可少, 因为第二步是在清理之前不满足条件的旧interval
            # 所以即使我们可以在第一步检查end time, 这里的题解省略了那一步, 放在第二步一并清理,逻辑更简洁
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # 3. 去除掉不符合条件的, 剩下的heap顶部第一个就是最小的区间,添加时不能简单的append,则要按照原有的original_index添加
            if min_heap:
                result[original_index] = min_heap[0][0]
            
        return result

