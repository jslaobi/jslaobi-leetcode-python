class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m = len(landStartTime)
        n = len(waterStartTime)

        min_time = float('inf')
        for i in range(m):
            for j in range(n):
                land_time_1 = landStartTime[i] + landDuration[i]
                water_time_1 = max(land_time_1, waterStartTime[j]) + waterDuration[j]
                
                water_time_2 = waterStartTime[j] + waterDuration[j]
                land_time_2 = max(water_time_2, landStartTime[i]) + landDuration[i]

                min_time = min(min_time, water_time_1, land_time_2)
        
        return min_time
