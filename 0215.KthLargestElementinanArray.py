import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        时间复杂度: O(n log k)，n 为数组长度，k 为第 k 个最大元素。
        空间复杂度: O(k)。
        """
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            # 当寻找第k个最大值时,使用min_heap. 最顶上的那个值即为第k个最大值
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return min_heap[0]