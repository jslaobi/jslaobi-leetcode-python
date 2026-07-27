import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        result = []

        for num in nums:
            # 如果是升序的, 就添加到数组的尾部
            if len(result) == 0 or num > result[-1]:
                result.append(num)
            else:
                # 否则就二分查找,将第一个比num大的数替换成num
                index = bisect.bisect_left(result, num)
                result[index] = num
        
        return len(result)