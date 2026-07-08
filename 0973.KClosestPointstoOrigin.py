class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        时间复杂度: O(n log k)。
        空间复杂度: O(k)。
        """
        max_heap = []

        for x, y in points:
            # 因为是到原点的距离,所以是x-0和y-0
            distance = x ** 2 + y ** 2
            # python里实现max heap的方式就是往里面推负数
            # 当推tuple进heap时, python会根据tupli里的值从左到右排序,所以distance会最先被用来排序
            heapq.heappush(max_heap, (-distance, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []

        for _dist, x, y in max_heap:
            result.append([x,y])
        
        return result