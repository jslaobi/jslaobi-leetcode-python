from collections import deque

class RecentCounter:

    def __init__(self):
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        self.queue = deque()

    def ping(self, t: int) -> int:
        # 添加到queue的结尾, 删除从queue的顶部
        self.queue.append(t)

        # 自我清洁, 每次添加时检查过期的记录
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()
        
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)