class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        result = []

        # 当只有一个区间时, 之后也不再会有交集
        while i < len(firstList) and j < len(secondList):
            start_a, end_a = firstList[i]
            start_b, end_b = secondList[j]

            # 两者的交集一定是较大的那个起点和较小的那个终点
            overlap_start = max(start_a, start_b)
            overlap_end = min(end_a, end_b)

            if overlap_start <= overlap_end:
                result.append([overlap_start, overlap_end])
            
            # 移动那个靠前的区间(终点较小的区间)
            if end_a < end_b:
                i += 1
            else:
                j += 1

        return result
        

