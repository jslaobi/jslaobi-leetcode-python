from collections import deque
class MyStack:

    def __init__(self):
        """
        时间复杂度: push O(n)，pop/top/empty O(1)。
        空间复杂度: O(n)。
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        for i in range(len(self.queue) - 1):
            item = self.queue.popleft()
            self.queue.append(item)

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()