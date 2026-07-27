from collections import deque

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        """时间复杂度: O(E log E)。
        空间复杂度: O(E + V)。
        """
        # 反转graph,将所有指向节点0的箭头转为由节点0指向其他节点
        reversed_graph = [[] for _ in range(n)]
        max_weight = 0

        # 反转graph, 同时找出最大weight
        for u, v, w in edges:
            reversed_graph[v].append((u,w))
            max_weight = max(max_weight, w)
        
        # 帮助寻找limit,也就是如果在当前的limit下, 所有的node是否都能连接到node 0
        def can_reach_all(limit):
            visited = [False] * n
            visited[0] = True

            queue = deque()
            queue.append(0)
            count = 1

            while queue:
                curr = queue.popleft()
                for neighbor, weight in reversed_graph[curr]:
                    if not visited[neighbor] and weight <= limit:
                        visited[neighbor] = True
                        count += 1
                        queue.append(neighbor)
            
            return count == n
        
        left = 1
        right = max_weight
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            if can_reach_all(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result