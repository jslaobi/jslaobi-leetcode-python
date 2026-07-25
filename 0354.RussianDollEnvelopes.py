import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))

        heights = []
        for env in envelopes:
           heights.append(env[1])

        result = []

        for height in heights:
            # 二分查找,找到插入height的合适位置
            index = bisect.bisect_left(result, height)

            if index == len(result):
                result.append(height)
            else:
                # 这里要考虑一种可能, 如果heights是[10, 20, 30, 1, 2, 3, 4], 我们如果只按照越来越大添加,最后得到的是[10, 20, 30]
                # 但是答案其实是[1, 2, 3, 4], 所以我们还要实时的将更小的值更新到result数组
                result[index] = height
        
        return len(result)