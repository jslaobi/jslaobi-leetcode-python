class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        # 分钟指针每分钟移动6度(360度除以60分钟)
        minute_angle = minutes * 6

        # 小时指针的范围是1 <= hour <= 12, 如果hour=12,按照0计算,所以先hour % 12
        # 小时指针每小时移动30度(360度除以12小时)
        # 同时,还要加上每分钟移动0.5度(30度除以60分钟), 比如3点半, 指针会在3和4之间的3.5的位置
        hour_angle = (hour % 12) * 30 + (minutes * 0.5)

        angle_diff = abs(hour_angle - minute_angle)

        # 按照题目要求, 返回比较小的角度
        if angle_diff > 180:
            return 360 - angle_diff
        else:
            return angle_diff