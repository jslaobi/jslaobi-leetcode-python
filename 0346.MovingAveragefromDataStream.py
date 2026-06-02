from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
    
    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            old_num = self.queue.popleft()
            self.sum -= old_num
        
        self.queue.append(val)
        self.sum += val

        return self.sum / len(self.queue)