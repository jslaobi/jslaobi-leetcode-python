class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        # arr示例:[40, 10, 20, 30]
        # sorted_set示例:[10,20,30,40]
        sorted_set = sorted(set(arr))
        # rank_map示例:{10:1, 20:2, 30:3, 40:4}
        rank_map = {}

        for i in range(len(sorted_set)):
            rank_map[sorted_set[i]] =  i + 1
        
        result = []

        for num in arr:
            result.append(rank_map[num])
        
        return result
