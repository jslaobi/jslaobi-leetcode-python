import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        时间复杂度: O(k log n)。
        空间复杂度: O(n)。
        """
        # 这道题不能用双指针, 会漏掉一些情况. 需要用min heap
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []

        # 如果从一个点开始,向下和向右探索,那么先向下后向右和先向右后向下就会重复
        # 为了避免重复,需要先把第一列加进来,然后向右探索
        # 探索第一列的长度是k和len(nums1)的较小值
        rows_to_initialize = min(k, len(nums1))

        for i in range(rows_to_initialize):
            # tuple值为两数之和, nums1的index, nums2的index
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(result) < k:
            # Pop the smallest sum from the heap
            current_sum, i, j = heapq.heappop(min_heap)
            
            # Add the actual pair of numbers to our result list
            result.append([nums1[i], nums2[j]])
            
            # 3. If there is a next element in nums2 for this row, push it to the heap!
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return result