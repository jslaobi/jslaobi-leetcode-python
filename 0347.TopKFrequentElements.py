class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
        
        result = []
        # len(freq) - 1也可以写成len(nums), 0也可以写作-1, 但是-1会检查freq[0],而不会有数字是频率0,所以一般写作0而不是-1
        for i in range(len(freq) - 1, 0, -1):
            # 别忘了freq里存的是一个个数组
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
