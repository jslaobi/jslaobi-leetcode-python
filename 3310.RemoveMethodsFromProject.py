class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        """时间复杂度: O(n + e)。
        空间复杂度: O(n + e)。
        """
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        is_suspicious = [False] * n
        is_suspicious[k] = True

        stack = [k]

        while stack:
            u = stack.pop()
            for v in graph[u]:
                # 如果is_suspicious[v]是False
                if not is_suspicious[v]:
                    is_suspicious[v] = True
                    stack.append(v)
        
        # 题目要求: healthy->buggy不行, 所以返回原数组
        for u, v in invocations:
            if not is_suspicious[u] and is_suspicious[v]:
                return list(range(n))
        
        # 如果buggy->buggy或者buggy->healthy是可以的, 返回所有不在is_suspicious数组里的元素
        return [i for i in range(n) if not is_suspicious[i]]
