import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """时间复杂度: O(n log n + q log n)。
        空间复杂度: O(n)。
        """
        # subsequence - 不需要连续,随意选取 
        # subarray - 需要连续
        nums.sort()

        prefix_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)
        
        result = []

        for q in queries:
            max_length = bisect.bisect_right(prefix_sum, q)
            result.append(max_length)
        
        return result