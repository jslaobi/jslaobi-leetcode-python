class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        """时间复杂度: O(E + V)。
        空间复杂度: O(E + V)。
        """
        n = len(scores)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            # 将节点的neighbor按照score降序排序(高score在前)
            graph[i].sort(key=lambda x:scores[x], reverse=True)
            # 保留前3高的score, 保留3个是因为要留出一些备选的选项,当第一score重复的时候,可以选择第二第三高的选项
            # 保留选项的数量是3,因为总共选出4个,所以当前节点最多需要跟另外3个节点组成4个节点的结果.如果题目要求结果是5个节点,则需要4个备选选项
            graph[i] = graph[i][:3]

        max_score = -1

        # 首先选定b和c(b和c两者是连接的), 然后往两边扩展确定a和d
        # u - 节点b v - 节点c
        for u, v in edges:
            # a - 节点a, a与b相连
            for a in graph[u]:
                # d - 节点d, d与c相连
                for d in graph[v]:
                    # 四个节点必须不相同
                    if a != v and d != u and a != d:
                        curr_score = scores[a] + scores[u] + scores[v] + scores[d]
                        max_score = max(max_score, curr_score)
        
        return max_score


