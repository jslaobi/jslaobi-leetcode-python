import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        def can_finish(k: int) -> bool:
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            # 按照题目要求, 等于也算合格
            return count <= h
        
        low = 1
        high = max(piles)
        speed = high
        # 这里用<=因为要找到那个准确的值
        while low <= high:
            mid = low + (high - low) // 2
            # 如果能完成,则记录当前找到的速度,并且将high更新成mid-1
            if can_finish(mid):
                speed = mid
                high = mid - 1
            else:
                # 如果能完成,则仅将low更新成mid+1
                low = mid + 1
        
        return speed