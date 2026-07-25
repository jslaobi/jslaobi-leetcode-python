class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """时间复杂度: O(V + E)。
        空间复杂度: O(V)。
        """
        n = len(graph)

        # 0 = Unvisited
        # 1 = Visiting (currently in our DFS path)
        # 2 = Safe (fully explored, no cycles found)
        state = [0] * n

        def dfs(node: int) -> bool:
            # 如果state不是0, 则说明是1或者2,如果是2,已证实safe的,直接返回true.如果是1,说明出现了环,返回false
            if state[node] != 0:
                return state[node] == 2
            
            state[node] = 1

            # 探索所有neighbor
            for neighbor in graph[node]:
                # 只要有一个unsafe, 整个node就unsafe, 返回False
                if not dfs(neighbor):
                    return False
            
            state[node] = 2
            return True
        
        safe_nodes = []
        for i in range(n):
            # dfs里传入的i是int,用graph[i]取真正的node
            if dfs(i):
                safe_nodes.append(i)
        
        return safe_nodes