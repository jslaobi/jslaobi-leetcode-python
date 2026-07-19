class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """时间复杂度: O(log n)。
        空间复杂度: O(1)。
        """
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 如果越界而没有大于target的数,返回第一个元素
        if left == len(letters):
            return letters[0]
        
        return letters[left]
