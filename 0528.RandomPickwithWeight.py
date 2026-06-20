class Solution:

    def __init__(self, w: List[int]):
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        # 比如[1, 3, 2], prefix_sum就是[1, 4, 6]
        self.prefix_sum = []
        # 帮助计算prefix_sum
        current_sum = 0

        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)
        
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        # 重量从1开始到total_sum
        # randint和range不同, 它包括1和total_sum
        target = random.randint(1, self.total_sum)

        left = 0
        right = len(self.prefix_sum) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.prefix_sum[mid] == target:
                return mid
            elif self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # 如果落在区间中间, 返回左边界
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()