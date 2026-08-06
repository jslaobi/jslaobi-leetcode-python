from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """时间复杂度: O(E log E)。
        空间复杂度: O(E)。
        """
        adj = defaultdict(list)

        # 题目要求按字母从小到大排序, 这里使用stack并从大到小排序依次pop,也可以使用queue并从小到大popleft,但是一般题解都是使用stack的多些
        for source, destination in sorted(tickets, reverse=True):
            adj[source].append(destination)
        
        result = []

        # Hierholzer's Algorithm using DFS
        def dfs(airport):
            # 将airport相连的机场一个个pop, 通过dfs找到最终的终点,依次加入result
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            
            result.append(airport)
        
        dfs("JFK")

        # 因为dfs的顺序是从最后一个机场往前添加, 所以结果要再反转一下才能得到正序
        return result[::-1]

