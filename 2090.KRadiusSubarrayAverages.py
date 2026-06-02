class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        # 两个半径加中心点
        window_size = 2 * k + 1
        if n < window_size:
            return result
        
        current_sum = sum(nums[:window_size])

        result[k] = current_sum // window_size
        # 将圆心向前移动,从k+1开始(初始时已经处理了k)
        for i in range(k + 1, n - k):
            # 将新圆心的右边+1,左边-1
            # 比如圆心在i=4,半径为空3. 最右边就是i+k=4+3=7,最左边是4-3=1,要移除的是4-3-1=0
            current_sum += nums[i + k] - nums[i - k - 1]
            result[i] = current_sum // window_size
        
        return result