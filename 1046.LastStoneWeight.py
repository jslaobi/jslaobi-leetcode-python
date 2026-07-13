class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        # 使用max_heap, 但是python里没有max_heap, 所以将所有值先转换为负数
        max_heap = [-stone for stone in stones]

        heapq.heapify(max_heap)

        # 至少有两个石头才能碰撞
        while(len(max_heap) > 1):
            # 最重的石头
            stone1 = heapq.heappop(max_heap)
            # 第二重的石头
            stone2 = heapq.heappop(max_heap)

            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)
        
        if max_heap:
            # 记得将值反转回来
            return -max_heap[0]
        # 最后两块石头同时消耗掉了
        else:
            return 0