class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """BFS 计算最少跳跃次数。

        时间复杂度: O(n)，n 为数组长度。
        空间复杂度: O(n)，用于图映射和队列。
        """
        length = len(arr)

        if length <= 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        queue = deque([0])
        visited = {0}
        steps = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node == length - 1:
                    return steps
                
                left = node - 1
                right = node + 1
                if left >=0 and left not in visited:
                    visited.add(left)
                    queue.append(left)
                if right < length and right not in visited:
                    visited.add(right)
                    queue.append(right)
                
                val = arr[node]
                for neighbor in graph[val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                
                graph[val].clear()

            steps += 1
        
        return -1