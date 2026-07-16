import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.array = nums.copy()

    def reset(self) -> List[int]:
        self.array = self.original.copy()
        return self.array

    def shuffle(self) -> List[int]:
        n = len(self.array)

        # 将每一个位置的i跟0到i随机位置的j交换
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()