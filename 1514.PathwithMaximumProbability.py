from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """时间复杂度: O(E log V)。
        空间复杂度: O(E + V)。
        """
        graph = defaultdict(list)
        for i, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_heap = []
        # 因为接下来的概率要相乘, 所以不是以0而是以1开始
        max_heap.append((-1.0, start_node))
        visited = set()

        while max_heap:
            prob, node = heapq.heappop(max_heap)

            if node == end_node:
                return -prob
            
            if node in visited:
                continue
            
            visited.add(node)

            # 探索邻居
            for neighbor, edge_prob in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(max_heap, ((prob * edge_prob, neighbor)))
        
        return 0.0