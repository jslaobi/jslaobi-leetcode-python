from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """时间复杂度: O(C + E)。
        空间复杂度: O(C + E)。
        """
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()

        in_degree = {}
        for word in words:
            for char in word:
                in_degree[char] = 0

        n = len(words) 
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))

            # 像["apple", "app"]这种情况是无效的
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    u, v = word1[j], word2[j]

                    # 如果是一个没见过的新规则,加入u和v的连接,v的in degree+1
                    if v not in adj[u]:
                        adj[u].add(v)
                        in_degree[v] += 1

                    # 当我们遇见第一个不同后,记录下来并且终止循环. 因为后面的字符先后顺序不能说明任何规则,如果继续处理反而错了
                    break

        # 没有prerequisites, 也就是(in_degree == 0)的可以开始处理
        queue = deque()
        for char in in_degree:
            if in_degree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            # 当in degree等于0时, 我们就加入结果. in degree代表有多个字符在当前字符之前, 比如in degree是3, 就说明有3个字符在之前,所以还不能加入结果
            result.append(char)

            # 加入结果后,就可以解锁后续字符了, in degree-1
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 这句检查是为了防止环出现, 也就是题目中的实例3:zxz的情况. 因为x和z相互依赖,所以最后无法处理完,in degree不会成为0, 也不会添加到result
        # 所以in degree的长度会大于result,这种情况会被认定为无效的情况, 返回空字符串
        if len(result) != len(in_degree):
            return ""
        else:
            return "".join(result)

        