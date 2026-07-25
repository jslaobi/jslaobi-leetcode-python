import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """时间复杂度: O(E log V)。
        空间复杂度: O(E + V)。
        """
        # 构建graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # heap存储(total_time, node),从time 0和node k开始
        min_heap = []
        min_heap.append((0,k))
        visited = set()

        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)
            max_time = time

            for neighbor, travel_time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + travel_time, neighbor))
            
        # 检查是否遍历了所有节点
        if len(visited) == n:
            return max_time
        else:
            return -1

        