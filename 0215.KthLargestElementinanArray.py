import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            # 当寻找第k个最大值时,使用min_heap. 最顶上的那个值即为第k个最大值
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return min_heap[0]