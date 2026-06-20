class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                # 数组是从0开始的,所以要+1
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        