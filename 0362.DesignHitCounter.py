from collections import deque

class HitCounter:
    def __init__(self):
        # 记录当前的秒数timestamp
        self.times = [0] * 300
        # 记录对应的hits数量
        self.hits = [0] * 300
    
    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        # 如果当前timestamp和记录的timestamp不一样, 说明这个位置的记录过期了, 更新当前timestamp, 并且重置hits数量为1
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            # 否则说明这个位置的记录还没有过期, 直接在原有的基础上加1个hit
            self.hits[index] += 1
    
    def getHits(self, timestamp: int) -> int:
        total_hits = 0
        for i in range(300):
            # 如果当前timestamp和记录的timestamp相差不超过300秒, 说明这个位置的记录还没有过期, 将hits数量加到total_hits上
            if timestamp - self.times[i] < 300:
                total_hits += self.hits[i]
        
        return total_hits
    
    # def __init__(self):
    #     self.queue = deque()
    
    # def hit(self, timestamp: int) -> None:
    #     self.queue.append(timestamp)
    
    # def getHits(self, timestamp: int) -> int:
    #     while self.queue and timestamp - self.queue[0] >= 300:
    #         self.queue.popleft()
    
    #     return len(self.queue)