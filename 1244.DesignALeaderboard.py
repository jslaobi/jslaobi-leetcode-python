import heapq
from collections import defaultdict

class Leaderboard:
    def __init__(self):
        self.scores = defaultdict(int)
    
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
    
    def top(self, K: int) -> int:
        min_heap = []

        for score in self.scores.values():
            heapq.heappush(min_heap, score)

            if len(min_heap) > K:
                heapq.heappop(min_heap)
        
        return sum(min_heap)
    
    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]