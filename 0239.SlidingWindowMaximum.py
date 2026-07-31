from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """时间复杂度: O(n)。
        空间复杂度: O(k)。
        """
        result = []

        # queue里存储每个数的index
        queue = deque()

        for i in range(len(nums)):
            # 将掉出窗口的数字移除
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            
            # 保持queue里的数字递减, 当nums[i]比queue里的数字大, 开始pop queue里的数字,直到为空或者queue里没有更小的数字为止
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            
            queue.append(i)

            # 一旦i达到k-1, 我们就要开始记录窗口最大值了. 因为queue是递减的,最大值就是queue[0]
            if i >= k - 1:
                result.append(nums[queue[0]])
        
        return result
            
