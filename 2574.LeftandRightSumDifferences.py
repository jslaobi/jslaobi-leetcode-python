class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        for num in nums:
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
        
        return answer
