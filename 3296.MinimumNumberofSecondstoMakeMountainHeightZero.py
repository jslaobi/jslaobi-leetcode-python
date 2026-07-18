class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        min_heap = []
        for w in workerTimes:
            # (next_completion_time, base_time, units_done_so_far)
            min_heap.append((w, w, 0))

        heapq.heapify(min_heap)

        result = 0

        for i in range(mountainHeight):
            time, w, units_done = heapq.heappop(min_heap)
            # 注意不是result += time, 工人们可以同时工作,我们用time累加时间而不是result
            result = time
            units_done += 1

            # 下一个工作需要的时间是w * (units_done + 1), 再加上time(用time累加时间)
            next_time = time + (w * (units_done + 1))

            heapq.heappush(min_heap, (next_time, w, units_done))
        
        return result