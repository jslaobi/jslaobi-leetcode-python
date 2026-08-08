from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """时间复杂度: O(n + u log u)。
        空间复杂度: O(u)。
        """
        freq_map = Counter(arr)

        sorted_frequences = sorted(freq_map.values())

        unique_count = len(sorted_frequences)

        # 按照出现次数从小到大排列,优先移除出现次数少的,如果剩余的k大于出现次数,就可以移除
        for freq in sorted_frequences:
            if k >= freq:
                k -= freq
                unique_count -= 1
            else:
                break
                
        return unique_count